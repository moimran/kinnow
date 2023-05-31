from api.device_account.schemas import DeviceAccountCreateSchema, TimeSchema
from api.device_account.services import DeviceAccountService
from db.db import db_session
from db.models.device_account import DeviceAccount
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get("/", response_model=list[TimeSchema])
async def get_device_accounts(
    session: AsyncSession = Depends(db_session),
) -> list[DeviceAccount]:
    device_account_service = DeviceAccountService(session=session)
    return await device_account_service.get_all_device_accounts()


@router.post("/", response_model=TimeSchema)
async def create_device_account(
    data: DeviceAccountCreateSchema,
    session: AsyncSession = Depends(db_session),
) -> DeviceAccount:
    device_account_service = DeviceAccountService(session=session)
    return await device_account_service.add_device_account(data)
