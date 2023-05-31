from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class DeviceAccountCreateSchema(BaseModel):
    username: str = Field(max_length=16)
    password: str = Field(
        min_length=8, max_length=16
    )
    enable_password: str = Field(
        min_length=8, max_length=16
    )
    description: Optional[str]


class TimeSchema(DeviceAccountCreateSchema):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]