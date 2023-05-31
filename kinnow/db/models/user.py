from db.models.common import UUIDModel
from sqlmodel import Field
from sqlalchemy import UniqueConstraint


class User(UUIDModel, table=True):

    __tablename__ = "Users"

    email: str = Field(nullable=False, max_length=50, index=True)
    password: str = Field(nullable=False)

    __table_args__ = (UniqueConstraint("email"),)

    def __repr__(self):
        return f"User(id={self.id}, email={self.email}, password={self.password})"
