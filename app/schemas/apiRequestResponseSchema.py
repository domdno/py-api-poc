from pydantic import BaseModel

class ApiRequestResponseSchema(BaseModel):
    request_data: dict
    response_data: dict