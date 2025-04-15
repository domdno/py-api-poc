from pydantic import BaseModel

class Consent(BaseModel):
    name: str
    status: str

    class Config:
        from_attributes = True