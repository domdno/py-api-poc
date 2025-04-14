from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db

from app.schemas.getLatestConsentsReponseSchema import GetLatestConsentsResponse
from app.domain.services.getAllLatestConsentsService import get_all_latest_consents
from app.domain.services.getSingleLatestConsentsService import get_single_latest_consents

get_latest_consents_router = APIRouter()

@get_latest_consents_router.get("/patients/latestconsents/{mdm_id}", response_model=GetLatestConsentsResponse)
async def get_lastest_consents_endpoint(
    mdm_id: str,
    consent: str | None = None,
    db: Session = Depends(get_db)
):
    try:
        if consent is None:
            latest_consents = get_all_latest_consents(mdm_id, db)
        else:
            latest_consents = get_single_latest_consents(mdm_id, consent, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return GetLatestConsentsResponse(data=latest_consents)