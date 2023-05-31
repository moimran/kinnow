from fastapi import FastAPI, status, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from api.users.services import UserService
from api.users.schemas import UserOut, UserAuth, TokenSchema, SystemUser
from fastapi import APIRouter, Depends
from db.db import db_session
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import Any
from utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password,
)

router = APIRouter()


@router.get("/", response_model=list[UserOut])
async def get_users(
    session: AsyncSession = Depends(db_session),
) -> list[UserAuth]:
    example_service = UserService(session=session)
    return await example_service.get_all_users()


@router.post("/", response_model=UserOut)
async def create_user(
    data: UserAuth,
    session: AsyncSession = Depends(db_session),
) -> Any:
    example_service = UserService(session=session)
    return await example_service.add_user(data)


@router.post(
    "/login",
    summary="Create access and refresh tokens for user",
    response_model=TokenSchema,
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(db_session),
):
    example_service = UserService(session=session)
    user = await example_service.get_user(form_data.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password"
        )

    hashed_pass = user["password"]
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(user["email"]),
        "refresh_token": create_refresh_token(user["email"]),
    }


# @router.get(
#     "/me", summary="Get details of currently logged in user", response_model=UserOut
# )
# async def get_me(user: SystemUser = Depends(get_current_user)):
#     return user
