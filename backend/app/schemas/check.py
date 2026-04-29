from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CheckCreate(BaseModel):
    service_id: int
    status: str
    response_time_ms: int | None = None


class CheckResponse(BaseModel):
    id: int
    service_id: int
    status: str
    response_time_ms: int | None
    checked_at: datetime

    model_config = ConfigDict(from_attributes=True)