from api.device_account.schemas import DeviceAccountCreateSchema
from db.db import db_session
from db.models.device_account import DeviceAccount
from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


class DeviceAccountService:
    def __init__(self, session: AsyncSession = Depends(db_session)):
        self.session = session

    async def get_all_device_accounts(self) -> list[DeviceAccount]:
        examples = await self.session.execute(select(DeviceAccount))

        return examples.scalars().fetchall()

    async def add_device_account(self, data: DeviceAccountCreateSchema) -> DeviceAccount:
        device_account_data = DeviceAccount(**data.dict())

        try:
            self.session.add(device_account_data)
            await self.session.commit()
            await self.session.refresh(device_account_data)
        except IntegrityError as e:
            # If the exception is a UniqueConstraint violation, return a 409 Conflict response
            if "duplicate key value violates" in str(e):
                if "DeviceAccount_username_key" in str(e):
                    raise HTTPException(
                        status_code=409, detail="User with this username already exists"
                    )
                if "DeviceAccount_email_key" in str(e):
                    raise HTTPException(
                        status_code=409, detail="User with this email already exists"
                    )
            # Otherwise, re-raise the exception
            raise e

        return device_account_data
