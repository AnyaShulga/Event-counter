from datetime import date

from pydantic import BaseModel


class EventBase(BaseModel):
    id: int
    event: str

    class Config:
        orm_mode = True


class User(BaseModel):
    ip: str
    id: int
    is_auth: bool

    class Config:
        orm_mode = True


class EventWithUser(BaseModel):
    event_id: int
    client_ip: str
    id: int
    date: date
    is_auth: bool

    class Config:
        orm_mode = True


class EventCount(BaseModel):
    event_id: int
    event_number: int

