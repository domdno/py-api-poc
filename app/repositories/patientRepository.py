from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.patient import Patient

async def save_patient(patient: Patient, db: AsyncSession) -> Patient:
    db.add(patient)
    await db.flush() # get patient.row_id
    return patient