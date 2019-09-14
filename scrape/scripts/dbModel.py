# Import Functions

from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///rubs.db')

Base = declarative_base()


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

    def __repr__(self):
       return "<Representative(Forename='%s', Surname='%s')>" % (
                            self.forename, self.surname)


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
    meetingType = relationship("MeetingType", back_populates='meetings')


class MeetingAttendance(Base):
    __tablename__ = "meetingAttendance"

    meetAttID = Column(Integer, primary_key=True)
    meetID = Column(Integer, ForeignKey('meetings.meetID'))
    repID = Column(Integer, ForeignKey('representatives.repID'))


#Organisation.representatives = relationship("Representative", order_by=Representative.id, back_populates="organisation")
Base.metadata.create_all(engine)
