#from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Date, Text
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
from datetime import datetime

import sqlalchemy as db
from sqlalchemy.sql import and_

import baseinfo
import dbConnectionString

from schedProc import meet_infocouncil_scrape

#engine = db.create_engine('sqlite:///rubs.db')
# options are 'sqlite' or 'dev'
engine = db.create_engine(dbConnectionString.connection_string('sqlite'))

connection = engine.connect()
metadata = db.MetaData()
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


def meet_type_query(type=None):
    if not type:
        print("No meeting type provided")
        return []
    meet_q = db.select([meeting_types]).\
      where(meeting_types.columns.meetName == type)
    meet_p = connection.execute(meet_q)
    return meet_p.fetchall()


def org_update(new_org):
    #Check newOrg has an orgName field
    if not new_org['orgName']:
        print("Dictionary must contain an 'orgName'")
        return -1
    # Check if organisation already in the Table
    exist = db.select([organisations]).\
      where(organisations.columns.orgName == new_org['orgName'])
    ResultProxy = connection.execute(exist)
    ResultSet = ResultProxy.fetchall()

    print(len(ResultSet))
    print(ResultSet)

    # If it isn't then insert it
    if not ResultSet:
        ins = db.insert(organisations).\
          values(orgName=new_org['orgName'], shortName=new_org['shortName'])
        ResultProxy = connection.execute(ins)
    else:
        # there is already a record,
        # update it with the remaining information
        if new_org['shortName']:
            # read the resultset to get the id
            # then update the record with that ID
            if new_org['shortName'] != ResultSet[0][2]:
                # Update the record for id ResultSet[0][0]
                udt = db.update(organisations).\
                  where(organisations.columns.orgID == ResultSet[0][0]).\
                  values(shortName=new_org['shortName'])
                ResultProxy = connection.execute(udt)


def rep_update(new_rep):
    #Check newOrg has an orgName field
    if not new_rep['Surname']:
        print("Dictionary must contain a 'Surname'")
        return -1
    # Check if representative already in the Table
    exist = db.select([representatives]).\
      where(representatives.columns.surname == new_rep['Surname'])
    ResultProxy = connection.execute(exist)
    ResultSet = ResultProxy.fetchall()

    print(len(ResultSet))
    print(ResultSet)

    # If it isn't then insert it
    if not ResultSet:
        ins = db.insert(representatives).\
          values(surname=new_rep['Surname'],
                forename=new_rep['Forename'],
                imageUrl=new_rep['ImageUrl'])
        ResultProxy = connection.execute(ins)
    else:
        # there is already a record,
        # so update it with the remaining information
        if new_rep['Surname']:
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
    org_q = db.select([organisations]).\
      where(organisations.columns.shortName == meet_url['org_short'])
    org_p = connection.execute(org_q)
    org = org_p.fetchall()
    # Ensure that there is a result
    if len(org) != 1:
        print("Organisation short name doesn't exist, or exists multiple times,\
              please update organisations")
        return -1
    # Extract the organisation ID
    org_id = org[0][0]

    # read the meeting schedule into a variable
    meet_l = meet_infocouncil_scrape(url=meet_url['meet_sched_url'])
    #print(meet_l)
    # iterate over the list and populate the meetings table.
    for m in meet_l:
        print(m)
        if not m:
            continue
        # Parse the date
        if m['Date']:
            date_obj = datetime.strptime(m['Date'], '%d %b %Y')
        else:
            print("No Date field")
            continue
        # Create new meeting types as required
        # Check if type in table
        meet_r = meet_type_query(type=m['Type'])
        # If not insert it
        if not meet_r:
            ins = db.insert(meeting_types).values(meetName=m['Type'])
            ResultProxy = connection.execute(ins)
            meet_r = meet_type_query(type=m['Type'])
        # Get the meetingTypeID
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
                meetings.columns.meetDate == date_obj))
        meet_prox = connection.execute(meet_qry)
        meet_set = meet_prox.fetchall()
        print(meet_set)
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
                            meetType=ou['Type'])
                update = connection.execute(udt)

def meeting_text():
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
    for m in meet_set:
        print(m)

    #extract the date

    #identify the shortname for the organisations

    #identify the meeting types

    #get the recordID

    #concatomate into a filename

    #read the url and type and then save as a text file

    #add the filename to the database

# Populate Organisations
for new_org in baseinfo.organisations:
    #newOrg = baseinfo.organisations[o]
    org_update(new_org=new_org)

# Populate Representatives
for new_rep in baseinfo.representatives:
    #newOrg = baseinfo.organisations[o]
    rep_update(new_rep=new_rep)

new_meet_url = baseinfo.meetingUrl[0]
meetings_base(meet_url=new_meet_url)
meeting_text()
