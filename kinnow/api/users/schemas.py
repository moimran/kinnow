from api.common import TimestampModel, UUIDModel
from sqlmodel import Field, SQLModel
from pydantic import EmailStr


class UserOutSchema(UUIDModel):
    username: str
    email: EmailStr
    full_name: str
    disabled: bool


class UserInSchema(SQLModel):
    username: str
    email: EmailStr
    full_name: str
    password: str


class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    username: str | None = None
