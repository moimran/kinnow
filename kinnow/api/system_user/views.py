from api.system_user.schemas import SystemUserCreateSchema, TimeSchema
from api.system_user.services import SystemUserService
from db.db import db_session
from db.models.system_user import SystemUser
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get("/", response_model=list[TimeSchema])
async def get_examples(
    session: AsyncSession = Depends(db_session),
) -> list[SystemUser]:
    example_service = SystemUserService(session=session)
    return await example_service.get_all_system_users()


@router.post("/", response_model=TimeSchema)
async def create_example(
    data: SystemUserCreateSchema,
    session: AsyncSession = Depends(db_session),
) -> SystemUser:
    example_service = SystemUserService(session=session)
    example = await example_service.add_system_user(data)
    return example
