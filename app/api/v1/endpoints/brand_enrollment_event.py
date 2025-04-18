from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import async_get_db
from app.core.config import V1_BRAND_ENROLLMENT_CREATED

from app.schemas.brandEnrollmentCreatedSchema import BrandEnrollmentCreatedSchema
from app.domain.services.brandEnrollmentCreatedService import create_enrollment
from app.domain.services.landingDataService import landing_data_service

brand_enrollment_router = APIRouter()

@brand_enrollment_router.post(
        V1_BRAND_ENROLLMENT_CREATED,
        response_model=BrandEnrollmentCreatedSchema
)
async def create_enrollment_endpoint(
    payload: BrandEnrollmentCreatedSchema,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(async_get_db)
):
    background_tasks.add_task(
        landing_data_service,
        "POST",
        V1_BRAND_ENROLLMENT_CREATED,
        payload,
    )
    try:
        enrollment = await create_enrollment(payload, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return enrollment