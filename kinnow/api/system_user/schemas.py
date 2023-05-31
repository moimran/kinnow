from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, constr


class SystemUserCreateSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: constr(
        min_length=8, max_length=16
    )


class TimeSchema(SystemUserCreateSchema):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
