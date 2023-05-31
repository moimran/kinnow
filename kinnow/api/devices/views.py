from api.devices.schemas import DeviceSchema, TimeSchema
from api.devices.services import DeviceService
from db.db import db_session
from db.models.device import Device
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get("/", response_model=list[TimeSchema])
async def get_devices(
    session: AsyncSession = Depends(db_session),
) -> list[Device]:
    device_service = DeviceService(session=session)
    return await device_service.get_all_devices()


@router.post("/", response_model=TimeSchema)
async def create_device(
    data: DeviceSchema,
    session: AsyncSession = Depends(db_session),
) -> Device:
    device_service = DeviceService(session=session)
    return await device_service.add_device(data)
