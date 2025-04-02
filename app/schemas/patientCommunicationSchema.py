from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, model_validator

class PatientCommunicationSchema(BaseModel):
    value: str
    type: str
    is_primary: Optional[bool] = Field(alias="isPrimary", default=True)
    status: Optional[str] = None

    """
    We use model_validator to take either "number" or "address" from the JSON
        object and store it as "value"
    """
    @model_validator(mode="before")
    def unify_value_field(cls, values):
        if "number" in values:
            values["value"] = values.pop("number")
        elif "address" in values:
            values["value"] = values.pop("address")
        else:
            raise ValueError("Communication must include either 'number' or 'address'")
        return values