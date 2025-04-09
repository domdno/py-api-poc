from fastapi import FastAPI
from app.api.v1.endpoints.brand_enrollment_event import brand_enrollment_router
from app.api.middleware.logging_middleware import LoggingMiddleware

app = FastAPI()

app.include_router(brand_enrollment_router)

app.add_middleware(LoggingMiddleware)