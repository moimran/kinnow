from db.db import db_session
from db.models.user import User
from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from utils import get_hashed_password
from api.users.schemas import UserOut, UserAuth
from fastapi.encoders import jsonable_encoder


class UserService:
    def __init__(self, session: AsyncSession = Depends(db_session)):
        self.session = session

    async def get_all_users(self) -> list[User]:
        examples = await self.session.execute(select(User))

        return examples.scalars().fetchall()

    async def get_user(self, email: str) -> User:
        user = await self.session.execute(select(User).where(User.email == email))

        return jsonable_encoder(user.one()).get("User")

    async def add_user(self, user: UserAuth) -> User:
        device_account_data = User(email=user.email, password=get_hashed_password(user.password))
        try:
            self.session.add(device_account_data)
            await self.session.commit()
            await self.session.refresh(device_account_data)
        except IntegrityError as e:
            raise e

        return device_account_data
