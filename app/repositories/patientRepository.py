from sqlalchemy.orm import Session
from app.db.models.patient import Patient

def save_patient(patient: Patient, db: Session) -> Patient:
    db.add(patient)
    db.flush() # get patient.row_id
    return patient