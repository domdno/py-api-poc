from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import async_get_db

from app.schemas.brandEnrollmentCreatedSchema import BrandEnrollmentCreatedSchema
from app.domain.services.brandEnrollmentCreatedService import create_enrollment

brand_enrollment_router = APIRouter()

@brand_enrollment_router.post(
        "/brand/enrollment/created/",
        response_model=BrandEnrollmentCreatedSchema
)
async def create_enrollment_endpoint(
    payload: BrandEnrollmentCreatedSchema,
    db: AsyncSession = Depends(async_get_db)
):
    try:
        enrollment = await create_enrollment(payload, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return enrollment