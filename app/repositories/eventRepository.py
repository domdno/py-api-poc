from sqlalchemy.orm import Session
from app.db.models.event import Event

def save_event(event: Event, db: Session) -> Event:
    db.add(event)
    db.flush() # get event.row_id
    return event