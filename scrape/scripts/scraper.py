#from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Date, Text
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship

import sqlalchemy as db
import baseinfo
import dbConnectionString

#engine = db.create_engine('sqlite:///rubs.db')
# options are 'sqlite' or 'dev'
engine = db.create_engine(dbConnectionString.connectionString('sqlite'))

connection = engine.connect()
metadata = db.MetaData()
organisations = db.Table('organisations', metadata, autoload=True, autoload_with=engine)


def orgUpdate(newOrg):
    #Check newOrg has an orgName field
    if not newOrg['orgName']:
        print("Dictionary must contain an 'orgName'")
        return -1
    # Check if organisation already in the Table
    exist = db.select([organisations]).where(organisations.columns.orgName == newOrg['orgName'])
    ResultProxy = connection.execute(exist)
    ResultSet = ResultProxy.fetchall()

    print(len(ResultSet))
    print(ResultSet)

    # If it isn't then insert it
    if not ResultSet:
        ins = db.insert(organisations).values(orgName=newOrg['orgName'], shortName=newOrg['shortName'])
        ResultProxy = connection.execute(ins)
    else:
        # there is already a record, so update it with the remaining information
        if newOrg['shortName']:
            # read the resultset to get the id and then update the record with that ID
            if newOrg['shortName'] != ResultSet[0][2]:
                # Update the record for id ResultSet[0][0]
                udt = db.update(organisations).where(organisations.columns.orgID == ResultSet[0][0]).values(shortName=newOrg['shortName'])
                ResultProxy = connection.execute(udt)

for newOrg in baseinfo.organisations:
    #newOrg = baseinfo.organisations[o]
    orgUpdate(newOrg=newOrg)
