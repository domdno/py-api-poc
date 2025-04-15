from pydantic import BaseModel

class ConsentPreferencesOption(BaseModel):
    selected_option: str

    class Config:
        orm_mode = True