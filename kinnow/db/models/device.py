from api.common import TimestampModel, UUIDModel
from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint, TEXT, JSON


class Device(TimestampModel, UUIDModel, table=True):

    __tablename__ = "Devices"

    hostname: str = Field(nullable=False, index=True)
    ip_address: str = Field(nullable=False)
    device_type: str = Field(nullable=False)
    snmpv2c: str = Field(nullable=True)
    description: str = Field(nullable=True)

    __table_args__ = (UniqueConstraint("ip_address"),)

    def __repr__(self):
        return f"DeviceAccount(id={self.id}, username={self.username}, password={self.password}, enable_password={self.enable_password}, description={self.description}, created_at={self.created_at}, updated_at={self.updated_at})"
