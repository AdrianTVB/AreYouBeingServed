# Import Functions

from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Date, Text, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import dbConnectionString

#engine = create_engine('sqlite:///rubs.db')
# options are 'sqlite' or 'dev'
engine = create_engine(dbConnectionString.connection_string('dev'))

Base = declarative_base()

metadata = MetaData()


class Organisation(Base):
     __tablename__ = 'organisations'

     orgID = Column(Integer, primary_key=True)
     orgName = Column(String(100))
     shortName = Column(String(50))

     def __repr__(self):
        return "<Organisation(orgName='%s', shortName='%s')>" % (
                             self.orgName, self.shortName)


class Representative(Base):
    __tablename__ = 'representatives'

    repID = Column(Integer, primary_key=True)
    surname = Column(String(50))
    forename = Column(String(50))
    imageUrl = Column(String(200))
    orgID = Column(Integer, ForeignKey('organisations.orgID'))
    startDate = Column(Date())
    endDate = Column(Date())

    def __repr__(self):
       return "<Representative(Forename='%s', Surname='%s', ImageUrl='%s')>" % (
                            self.forename, self.surname, self.imageUrl)


class Role(Base):
    __tablename__ = 'roles'

    roleID = Column(Integer, primary_key=True)
    roleName = Column(String(50))

    def __repr__(self):
       return "<Role(Name='%s')>" % (
                            self.roleName)


class MeetingType(Base):
    __tablename__ = 'meetingTypes'

    meetTypeID = Column(Integer, primary_key=True)
    meetName = Column(String(100))

    def __repr__(self):
       return "<MeetingType(Name='%s')>" % (
                            self.meetName)


class MeetingRepRelationship(Base):
    __tablename__ = 'meetingRepRelationships'

    relID = Column(Integer, primary_key=True)
    orgID = Column(Integer, ForeignKey('organisations.orgID'))
    repID = Column(Integer, ForeignKey('representatives.repID'))
    meetTypeID = Column(Integer, ForeignKey('meetingTypes.meetTypeID'))
    startDate = Column(Date())
    endDate = Column(Date())

    organisation = relationship("Organisation", back_populates="meetingRepRelationships")
    representatives = relationship("Representative", back_populates='meetingRepRelationships')
    meetingType = relationship("MeetingType", back_populates='meetingTypes')


class Meetings(Base):
    __tablename__ = 'meetings'

    meetID = Column(Integer, primary_key=True)
    orgID = Column(Integer, ForeignKey('organisations.orgID'))
    meetTypeID = Column(Integer, ForeignKey('meetingTypes.meetTypeID'))
    meetDate = Column(Date())
    minuteUrl = Column(String(200))
    minuteType = Column(String(4)) # html or pdf
    minuteText = Column(Text())
    minuteFile = Column(String(50))

    organisation = relationship("Organisation", back_populates="meetings")
    meetingType = relationship("MeetingType", back_populates="meetings")
    meetingTypeScrapeHelper = relationship("MeetingTypeScrapeHelper", back_populates="meetings")


class MeetingAttendance(Base):
    __tablename__ = "meetingAttendance"

    meetAttID = Column(Integer, primary_key=True)
    meetID = Column(Integer, ForeignKey('meetings.meetID'))
    repID = Column(Integer, ForeignKey('representatives.repID'))

    meetings = relationship("Meeting", back_populates="meetingAttendance")
    representatives = relationship("Representative", back_populates="meetingAttendance")



class MeetingTypeScrapeHelper(Base):
    __tablename__ = "meetingTypeScrapeHelper"

    meetScrapeID = Column(Integer, primary_key=True)
    meetTypeID = Column(Integer, ForeignKey('meetingTypes.meetTypeID'))
    orgID = Column(Integer, ForeignKey('organisations.orgID'))
    startWord = Column(String(50))
    endWord = Column(String(50))



#Organisation.representatives = relationship("Representative", order_by=Representative.id, back_populates="organisation")

Base.metadata.create_all(engine)
metadata.create_all(engine)
