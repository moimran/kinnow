from api.system_user.schemas import SystemUserCreateSchema
from db.db import db_session
from db.models.system_user import SystemUser
from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


class SystemUserService:
    def __init__(self, session: AsyncSession = Depends(db_session)):
        self.session = session

    async def get_all_system_users(self) -> list[SystemUser]:
        examples = await self.session.execute(select(SystemUser))

        return examples.scalars().fetchall()

    async def add_system_user(self, data: SystemUserCreateSchema) -> SystemUser:
        system_user_data = SystemUser(**data.dict())

        try:
            self.session.add(system_user_data)
            await self.session.commit()
            await self.session.refresh(system_user_data)
        except IntegrityError as e:
            # If the exception is a UniqueConstraint violation, return a 409 Conflict response
            if "duplicate key value violates" in str(e):
                if "SystemUser_username_key" in str(e):
                    raise HTTPException(
                        status_code=409, detail="User with this username already exists"
                    )
                if "SystemUser_email_key" in str(e):
                    raise HTTPException(
                        status_code=409, detail="User with this email already exists"
                    )
            # Otherwise, re-raise the exception
            raise e

        return system_user_data
