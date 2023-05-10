from datetime import date

from pydantic.validators import IPv4Address
from sqlalchemy import func
from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, client_ip: str):
    db_user = db.query(models.User).filter_by(ip=client_ip).first()
    return db_user


def create_user_event(db: Session, event_id: int, client_ip: str, date: date, is_auth: bool):
    db_event = models.EventWithUser(event_id=event_id, client_ip=client_ip, date=date, is_auth=is_auth)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

