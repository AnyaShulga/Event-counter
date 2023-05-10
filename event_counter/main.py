import datetime
from datetime import date, datetime

from fastapi import Depends, FastAPI, Request, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/events/{event_id}", response_model=schemas.EventWithUser)
def create_user_with_event(event_id: int, request: Request, db: Session = Depends(get_db)):
    client_ip = request.client.host
    event = db.query(models.Event).filter_by(id=event_id).one_or_none()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    user = crud.get_user(db, client_ip)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    date = datetime.date(datetime.now())
    return crud.create_user_event(db=db, event_id=event.id, client_ip=user.ip, date=date, is_auth=user.is_auth)


@app.post("/events/", response_model=schemas.EventCount)
def read_event(
        date: date,
        event_id: int,
        ip: str | None = None,
        status: bool | None = None,
        db: Session = Depends(get_db),
):
    event_filter = db\
        .query(models.EventWithUser)\
        .filter_by(event_id=event_id)\
        .filter_by(date=date)
    if ip:
        event_filter = event_filter.filter_by(client_ip=ip)
    if status:
        event_filter = event_filter.filter_by(is_auth=status)
    event_number = event_filter.count()
    return schemas.EventCount(event_id=event_id, event_number=event_number)