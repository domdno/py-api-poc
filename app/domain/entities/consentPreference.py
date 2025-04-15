from pydantic import BaseModel

class ConsentPreference(BaseModel):
    name: str

    class Config:
        from_attributes = True