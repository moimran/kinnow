from api.common import TimestampModel, UUIDModel
from sqlmodel import Field
from sqlalchemy import UniqueConstraint
from pydantic import EmailStr
from typing import Optional


class User(TimestampModel, UUIDModel, table=True):

    __tablename__ = "User"

    username: str
    email: EmailStr
    full_name: Optional[str] = ""
    hashed_password: Optional[str] = ""
    disabled: Optional[bool] = False
