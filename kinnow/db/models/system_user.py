from db.models.common import TimestampModel, UUIDModel
from sqlmodel import Field
from sqlalchemy import UniqueConstraint


class SystemUser(TimestampModel, UUIDModel, table=True):

    __tablename__ = "SystemUser"

    username: str = Field(nullable=False, max_length=200, index=True)
    first_name: str = Field(nullable=False, max_length=200)
    last_name: str = Field(nullable=False, max_length=200)
    email: str = Field(nullable=False, max_length=200)
    password: str = Field(nullable=False, max_length=16, min_length=8)

    __table_args__ = (UniqueConstraint("email"), UniqueConstraint("username"))

    def __repr__(self):
        return f"SystemUser(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, password={self.password}, created_at={self.created_at}, updated_at={self.updated_at})"
