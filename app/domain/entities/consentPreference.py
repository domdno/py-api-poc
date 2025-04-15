from pydantic import BaseModel

class ConsentPreference(BaseModel):
    name: str

    class Config:
        orm_mode = True