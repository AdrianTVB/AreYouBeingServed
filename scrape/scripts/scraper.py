#from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Date, Text
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship

import sqlalchemy as db
import baseinfo
import dbConnectionString

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

# Populate Organisations
for new_org in baseinfo.organisations:
    #newOrg = baseinfo.organisations[o]
    org_update(new_org=new_org)

# Populate Representatives
for new_rep in baseinfo.representatives:
    #newOrg = baseinfo.organisations[o]
    rep_update(new_rep=new_rep)
