#from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Date, Text
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
from datetime import datetime
import os.path
import string
import unidecode

import sqlalchemy as db
from sqlalchemy.sql import and_
from sqlalchemy import join

import baseinfo
import dbConnectionString

from schedProc import meet_infocouncil_scrape
from url_to_text import html_to_txt, pdf_to_txt
from minProc import attendList, subString

#engine = db.create_engine('sqlite:///rubs.db')
# options are 'sqlite' or 'dev'
engine = db.create_engine(dbConnectionString.connection_string('sqlite'))

connection = engine.connect()
metadata = db.MetaData()

#fileDir="scrape/data/txt/scraped/dev/"
fileDir="scrape/data/txt/scraped/"

organisations = db.Table('organisations',
                            metadata,
                            autoload=True,
                            autoload_with=engine)

representatives = db.Table('representatives',
                            metadata,
                            autoload=True,
                            autoload_with=engine)

meetings = db.Table('meetings',
                            metadata,
                            autoload=True,
                            autoload_with=engine)

meeting_types = db.Table('meetingTypes',
                            metadata,
                            autoload=True,
                            autoload_with=engine)

meeting_rep_relationships = db.Table('meetingRepRelationships',
                            metadata,
                            autoload=True,
                            autoload_with=engine)

meeting_type_scrape_help = db.Table('meetingTypeScrapeHelper',
                            metadata,
                            autoload=True,
                            autoload_with=engine)

meeting_attendance = db.Table('meetingAttendance',
                            metadata,
                            autoload=True,
                            autoload_with=engine)

def meet_type_query(type=None):
    if not type:
        print("No meeting type provided")
        return []
    meet_q = db.select([meeting_types]).\
      where(meeting_types.columns.meetName == type)
    meet_p = connection.execute(meet_q)
    return meet_p.fetchall()


def org_id_lookup(shortName=None):
    # get the organisation ID corresponding to org_short
    org_q = db.select([organisations]).\
      where(organisations.columns.shortName == shortName)
    org_p = connection.execute(org_q)
    org = org_p.fetchall()
    # Ensure that there is a result
    if len(org) != 1:
        print("Organisation short name doesn't exist, or exists multiple times,\
              please update organisations")
        return -1
    else:
        # Extract the organisation ID
        return org[0][0]

def meet_type_id_lookup(meet_type_name=None):
    meet_q = db.select([meeting_types.columns.meetTypeID]).\
      where(meeting_types.columns.meetName == meet_type_name)
    meet_p = connection.execute(meet_q)
    meet_t = meet_p.fetchall()
    if len(meet_t) != 1:
        print("Meeting type doesn't exist, or exists multiple times,\
              please update meeting types")
        return -1
    else:
        # Return the meeting ID
        return meet_t[0][0]

def org_update(new_org):
    #Check newOrg has an orgName field
    if not new_org['orgName']:
        print("Dictionary must contain an 'orgName'")
        return -1
    # Check if organisation already in the Table
    print("Checking if %s already loaded." % new_org['orgName'])
    exist = db.select([organisations]).\
      where(organisations.columns.orgName == new_org['orgName'])
    ResultProxy = connection.execute(exist)
    ResultSet = ResultProxy.fetchall()
    # If it isn't then insert it
    if not ResultSet:
        print("Loading to database.")
        ins = db.insert(organisations).\
          values(orgName=new_org['orgName'],
                shortName=new_org['shortName'],
                mapName=new_org['mapName'],
                mapID=new_org['mapID'])
        ResultProxy = connection.execute(ins)
    else:
        print("Updating record.")
        # there is already a record,
        # update it with the remaining information
        if new_org['shortName']:
            # read the resultset to get the id
            # then update the record with that ID
            if new_org['shortName'] != ResultSet[0][2] or\
               new_org['mapName'] != ResultSet[0][3] or\
               new_org['mapID'] != ResultSet[0][4]:
                # Update the record for id ResultSet[0][0]
                udt = db.update(organisations).\
                  where(organisations.columns.orgID == ResultSet[0][0]).\
                  values(shortName=new_org['shortName'],
                        mapName=new_org['mapName'],
                        mapID=new_org['mapID'])
                ResultProxy = connection.execute(udt)


def rep_update(new_rep, orgShortName, start=None, end=None):
    #Check newOrg has an orgName field
    if not new_rep['Surname']:
        print("Dictionary must contain a 'Surname'")
        return -1
    # Check if representative already in the Table for the org and timeperiod
    # Look up the organisation ID for the shortname provided
    print("Checking if %s already loaded." % new_rep['Surname'])
    org_id = org_id_lookup(shortName=orgShortName)
    exist = db.select([representatives]).\
      where(and_(representatives.columns.surname == new_rep['Surname'],
                representatives.columns.orgID == org_id))
    ResultProxy = connection.execute(exist)
    ResultSet = ResultProxy.fetchall()
    # If it isn't then insert it
    if not ResultSet:
        print("Loading record to database.")
        ins = db.insert(representatives).\
          values(surname=new_rep['Surname'],
                forename=new_rep['Forename'],
                imageUrl=new_rep['ImageUrl'],
                orgID=org_id)
        ResultProxy = connection.execute(ins)
    else:
        # there is already a record,
        # so update it with the remaining information
        if new_rep['Surname']:
            print("Updating database.")
            # read the resultset to get the id
            # then update the record with that ID
            if new_rep['Forename'] != ResultSet[0][2] or\
              new_rep['ImageUrl'] != ResultSet[0][3]:
                # Update the record for id ResultSet[0][0]
                udt = db.update(representatives).\
                  where(representatives.columns.repID == ResultSet[0][0]).\
                  values(forename=new_rep['foreame'],
                        imageUrl=new_rep['forename'])
                ResultProxy = connection.execute(udt)

def meetings_base(meet_url=None):
    # Check valid dictionary provided
    if not meet_url['org_short'] or not meet_url['meet_sched_url']:
        print("A dictionary containing org_short and meet_sched_url must be provided")
        return -1
    # get the organisation ID corresponding to org_short
    org_id = org_id_lookup(shortName=meet_url['org_short'])
    print("Reading the meetings schedule for %s." % meet_url['org_short'])
    # read the meeting schedule into a variable
    meet_l = meet_infocouncil_scrape(url=meet_url['meet_sched_url'])
    #print(meet_l)
    # iterate over the list and populate the meetings table.
    print("Loading schedule to database.")
    for m in meet_l:
        #print(m)
        if not m:
            continue
        # Parse the date
        if m['Date']:
            date_obj = datetime.strptime(m['Date'], '%d %b %Y').date()
        else:
            print("No Date field")
            continue
        # Create new meeting types as required
        # Check if type in table
        # remove macrons from string first
        m['Type'] = unidecode.unidecode(m['Type'])
        meet_r = meet_type_query(type=m['Type'])
        # If not insert it
        if not meet_r:
            ins = db.insert(meeting_types).values(meetName=m['Type'])
            ResultProxy = connection.execute(ins)
            meet_r = meet_type_query(type=m['Type'])
        # Get the meetingTypeID
        #print("Meeting Type ID")
        #print(meet_r)
        m_type_id = meet_r[0][0]
        # Store the url for the html minutes in preference to the pdf one if both
        # url is a list with Type and url
        ou = None
        if m['url']:
            for u in m['url']:
                if u['Type'] == 'html':
                    ou = u
                elif u['Type'] == 'pdf' and not ou:
                    ou = u
        if not ou:
            ou = {'Type': None, 'url': None}

        # Load into database, or update if existing
        meet_qry = db.select([meetings]).\
          where(and_(meetings.columns.orgID == org_id,
                meetings.columns.meetTypeID == m_type_id,
                # Need to sort the comparison out datetime date to datetime object.
                meetings.columns.meetDate == date_obj))
        meet_prox = connection.execute(meet_qry)
        meet_set = meet_prox.fetchall()
        #print(meet_set)
        # If it isn't then insert it
        if not meet_set:
            ins = db.insert(meetings).\
              values(orgID=org_id,
                    meetTypeID=m_type_id,
                    meetDate=date_obj,
                    minuteUrl=ou['url'],
                    minuteType=ou['Type'])
            ResultProxy = connection.execute(ins)
        else:
            # there is already a record,
            # so update it with the remaining information
            if ou['url'] != None and meet_set[0][4] == None:
                # Update the record for id ResultSet[0][0]
                udt = db.update(meetings).\
                      where(meetings.columns.meetID == meet_set[0][0]).\
                      values(minuteUrl=ou['url'],
                            minuteType=ou['Type'])
                update = connection.execute(udt)

def meeting_text(fileDir="scrape/data/txt/scraped/"):
    # Get a list of meetings that have a url and no filename
    meet_qry = db.select([meetings]).\
      where(and_(meetings.columns.minuteUrl != None,
            meetings.columns.minuteFile == None))
    meet_prox = connection.execute(meet_qry)
    meet_set = meet_prox.fetchall()
    if not meet_set:
        print("No results to process")
        return
    # Iterate over the results
    print("Creating text files.")
    for m in meet_set:
        #print(m)
        #extract the date
        mdate = m[3].strftime("%Y%m%d")
        #identify the shortname for the organisations
        org_q = db.select([organisations.columns.shortName]).\
          where(organisations.columns.orgID == m[1])
        org_p = connection.execute(org_q)
        org = org_p.fetchall()[0][0]
        #print(org)
        #print(org[0][0])
        #identify the meeting type
        meet_q = db.select([meeting_types.columns.meetName]).\
          where(meeting_types.columns.meetTypeID == m[2])
        meet_p = connection.execute(meet_q)
        meet_t = meet_p.fetchall()
        #print(meet_t[0][0])
        # Clean the string and remove spaces
        meet_txt = ''.join(e for e in meet_t[0][0] if e.isalnum())
        #print(meet_txt)
        #get the recordID
        recID = str(m[0])
        # Truncate filename to fit in field
        str_max_len = 46 - len(recID)
        f_name_full = mdate + org + meet_txt
        #concatomate into a filename
        fname =  f_name_full[:str_max_len] + recID + '.txt'
        #read the url and type and then save as a text file
        text = ""
        if m[5] == 'html':
            text = html_to_txt(url=m[4])
        elif m[5] == 'pdf':
            text = pdf_to_txt(url=m[4])
        else:
            continue
        if text:
            print("Saving %s" % fname)
            with open(os.path.join(fileDir, fname), "w") as f:
                f.write(text)
            #add the filename to the database
            udt = db.update(meetings).\
                  where(meetings.columns.meetID == m[0]).\
                  values(minuteFile=fname)
            update = connection.execute(udt)


def meet_rep_all_pop(meet_all=None, start_date=None, end_date=None):
    if not meet_all:
        print("A list of dictionaries of meetings all representatives \
               are expected to attend is required")
        return -1
    # Iterate through the file
    print("Loading expected attendance (all councillors).")
    for e in meet_all:
        # Identify the organisation and meeting type
        # get the organisation ID corresponding to org_short
        org_id = org_id_lookup(shortName=e['org_short'])
        #identify the meeting type
        meet_type_id = meet_type_id_lookup(meet_type_name=e['meet_type'])
        # get a list of representatives for that org
        rep_q = db.select([representatives]).\
          where(representatives.columns.orgID == org_id)
        rep_p = connection.execute(rep_q)
        rep_l = rep_p.fetchall()
        for r in rep_l:
            # Insert data into the MeetingRepRelationShip table_row
            meetrep_qry = db.select([meeting_rep_relationships]).\
              where(and_(meeting_rep_relationships.columns.orgID == org_id,
                    meeting_rep_relationships.columns.repID == r[0],
                    meeting_rep_relationships.columns.meetTypeID == meet_type_id))
            meetrep_prox = connection.execute(meetrep_qry)
            meetrep_set = meetrep_prox.fetchall()
            #print(meetrep_set)
            # If it isn't then insert it
            if not meetrep_set:
                ins = db.insert(meeting_rep_relationships).\
                  values(orgID=org_id,
                        meetTypeID=meet_type_id,
                        repID=r[0])
                ResultProxy = connection.execute(ins)

def meet_rep_extra_pop(meet_extra=None, start_date=None, end_date=None):
    if not meet_extra:
        print("A list of dictionaries of meetings and the representatives \
               that are expected to attend is required")
        return -1
    # Iterate through the file
    print("Loading expected attendance.")
    for e in meet_extra:
        # Identify the organisation and meeting type
        # get the organisation ID corresponding to org_short
        org_id = org_id_lookup(shortName=e['org_short'])
        #identify the meeting type
        meet_type_id = meet_type_id_lookup(meet_type_name=e['meet_type'])
        # get a list of representatives for that org
        reps = e['representatives']
        for r in reps:
            rep_q = db.select([representatives]).\
              where(representatives.columns.surname == r)
            rep_p = connection.execute(rep_q)
            rep_l = rep_p.fetchall()
            if not rep_l:
                continue
            rep_id = rep_l[0][0]
            # Insert data into the MeetingRepRelationShip table_row
            meetrep_qry = db.select([meeting_rep_relationships]).\
              where(and_(meeting_rep_relationships.columns.orgID == org_id,
                    meeting_rep_relationships.columns.repID == rep_id,
                    meeting_rep_relationships.columns.meetTypeID == meet_type_id))
            meetrep_prox = connection.execute(meetrep_qry)
            meetrep_set = meetrep_prox.fetchall()
            #print(meetrep_set)
            # If it isn't then insert it
            if not meetrep_set:
                ins = db.insert(meeting_rep_relationships).\
                  values(orgID=org_id,
                        meetTypeID=meet_type_id,
                        repID=rep_id)
                ResultProxy = connection.execute(ins)

def scrape_help_update(new_helper):
    #Check new_helper has an orgshort and meeting type field
    if not new_helper['org_short'] or not new_helper['meet_type']:
        print("Dictionary must contain an 'org_short' and 'meet_type'")
        return -1
    # Lookup the org_id
    print("Loading start and stop text triggers.")
    org_id = org_id_lookup(shortName=new_helper['org_short'])
    # Lookup the meet_type_id
    meet_type_id = meet_type_id_lookup(meet_type_name=new_helper['meet_type'])
    # Check if entry already in the Table
    exist = db.select([meeting_type_scrape_help]).\
      where(and_(meeting_type_scrape_help.columns.orgID == org_id,
                meeting_type_scrape_help.columns.meetTypeID == meet_type_id))
    ResultProxy = connection.execute(exist)
    ResultSet = ResultProxy.fetchall()
    # If it isn't then insert it
    if not ResultSet:
        ins = db.insert(meeting_type_scrape_help).\
          values(orgID=org_id,
                meetTypeID=meet_type_id,
                startWord=new_helper['startWord'],
                endWord=new_helper['endWord'])
        ResultProxy = connection.execute(ins)
    else:
        # there is already a record,
        # update it with the remaining information
        if new_helper['startWord'] != ResultSet[0][3]:
            # Update the record for id ResultSet[0][0]
            udt = db.update(meeting_type_scrape_help).\
                 where(meeting_type_scrape_help.columns.meetScrapeID == ResultSet[0][0]).\
                 values(startWord=new_helper['startWord'],
                        endWord=new_helper['endWord'])
            ResultProxy = connection.execute(udt)


def attendance_update(fileDir="scrape/data/txt/scraped/"):
    # Get list of meetings with a text file
    j = meetings.join(meeting_type_scrape_help,
            and_(meeting_type_scrape_help.columns.orgID == meetings.columns.orgID,
                meeting_type_scrape_help.columns.meetTypeID == meetings.columns.meetTypeID))
    meet_qry = db.select([meetings,
                        meeting_type_scrape_help.columns.startWord,
                        meeting_type_scrape_help.columns.endWord]).\
                        select_from(j).\
                        where(and_(meetings.columns.minuteFile != None,
                        meeting_type_scrape_help.columns.startWord != None,
                        meeting_type_scrape_help.columns.endWord != None))
    meet_prox = connection.execute(meet_qry)
    meet_set = meet_prox.fetchall()
    if not meet_set:
        print("No results to process")
        return
    print("Updating attendance.")
    # iterate over the meetings and get the attendance.
    for m in meet_set:
        meet_id = m[0]
        org_id = m[1]
        meet_type_id = m[2]
        # retrieve list of reps for the organisation
        rep_q = db.select([representatives]).\
          where(organisations.columns.orgID == org_id)
        rep_p = connection.execute(rep_q)
        rep_r = rep_p.fetchall()
        rep = [r[1] for r in rep_r]
        # extract attendance from the text
        #fileDir = "scrape/data/txt/scraped/"
        f_name = m[7]
        s_word = m[8]
        e_word = m[9]
        with open(os.path.join(fileDir, f_name), "r") as f:
            raw_text = f.read()
        attend_text = subString(text=raw_text, startWord=s_word, endWord=e_word)
        attendance = attendList(attend_text, rep)
        exist = db.select([meeting_attendance]).\
          where(meeting_attendance.columns.meetID == meet_id)
        ResultProxy = connection.execute(exist)
        ResultSet = ResultProxy.fetchall()
        # If it isn't then insert it
        if not ResultSet:
            # Iterate through all of the representatives, get their ID and insert
            for a in attendance:
                rep_inf = next(r for r in rep_r if r[1] == a)
                ins = db.insert(meeting_attendance).\
                        values(meetID=meet_id,
                                repID=rep_inf[0])
                ResultProxy = connection.execute(ins)



# Populate Organisations
for new_org in baseinfo.organisations:
    #newOrg = baseinfo.organisations[o]
    org_update(new_org=new_org)

# Populate Representatives
for org_reps in baseinfo.representatives:
    for new_rep in org_reps['reps']:
    #newOrg = baseinfo.organisations[o]
        rep_update(new_rep=new_rep, orgShortName=org_reps['orgShortName'])

#new_meet_url = baseinfo.meetingUrl[0]
for new_meet_url in baseinfo.meetingUrl:
    meetings_base(meet_url=new_meet_url)

meeting_text(fileDir=fileDir)

meet_rep_all_pop(meet_all=baseinfo.meetingRepAll)

meet_rep_extra_pop(meet_extra=baseinfo.meetingRepExtra)

for h in baseinfo.meetingTypeScrapeHelp:
    scrape_help_update(new_helper=h)

attendance_update(fileDir=fileDir)
