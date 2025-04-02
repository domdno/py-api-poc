from fastapi import FastAPI
from app.api.v1.endpoints.brand_enrollment_event import brand_enrollment_router

app = FastAPI()

app.include_router(brand_enrollment_router)