from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.event import Event

async def save_event(event: Event, db: AsyncSession) -> Event:
    db.add(event)
    await db.flush() # get event.row_id
    return event