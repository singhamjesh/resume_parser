from pydantic import BaseModel


class StatusSchema(BaseModel):
    id: str


class ApiResponse(BaseModel):
    id: str
    status: str
    data: dict
