from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, IPvAnyAddress, Field


class DeviceSchema(BaseModel):
    hostname: str = Field(max_length=16)
    ip_address: str = Field(max_length=16)
    device_type: str = Field(max_length=16)
    password: str = Field(min_length=8, max_length=16)
    enable_password: str = Field(min_length=8, max_length=16)
    description: Optional[str]


class TimeSchema(DeviceSchema):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
