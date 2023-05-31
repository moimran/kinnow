from db.models.common import TimestampModel, UUIDModel
from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint, TEXT, JSON


class DeviceAccount(TimestampModel, UUIDModel, table=True):

    __tablename__ = "DeviceAccount"

    username: str = Field(nullable=False, max_length=50, index=True)
    password: str = Field(nullable=False)
    enable_password: str = Field(nullable=False)
    description: str = Field(nullable=True)

    def __repr__(self):
        return f"DeviceAccount(id={self.id}, username={self.username}, password={self.password}, enable_password={self.enable_password}, description={self.description}, created_at={self.created_at}, updated_at={self.updated_at})"
