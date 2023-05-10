from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    ip = Column(String, unique=True)
    is_auth = Column(Boolean)


class Event(Base):
    __tablename__ = "Events"
    id = Column(Integer, primary_key=True)
    event = Column(String)


class EventWithUser(Base):
    __tablename__ = "Event with User"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("Events.id"))
    client_ip = Column(String, ForeignKey("Users.ip"))
    date = Column(Date)
    is_auth = Column(Boolean, ForeignKey("Users.is_auth"))
