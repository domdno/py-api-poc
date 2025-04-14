from typing import List
from pydantic import BaseModel

from app.schemas.consentSchema import ConsentSchema

class GetLatestConsentsResponse(BaseModel):
    data: List[ConsentSchema]