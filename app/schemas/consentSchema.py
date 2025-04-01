from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ConsentSchema(BaseModel):
    name: str
    status: str