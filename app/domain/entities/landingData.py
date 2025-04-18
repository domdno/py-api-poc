from pydantic import BaseModel

class LandingData(BaseModel):
    request_method: str
    request_path: str
    request_data: dict

    class Config:
        from_attributes = True
