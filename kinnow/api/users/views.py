from datetime import timedelta
from api.users.services import (
    UserService,
    get_current_active_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from sqlmodel.ext.asyncio.session import AsyncSession

from fastapi import APIRouter, Depends, HTTPException, status, Request
from db.db import db_session

from db.models.user import User

from api.users.schemas import UserOutSchema, UserInSchema, Token

from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(db_session),
):
    user_service = UserService(session=session)
    user = await user_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await user_service.create_access_token(
        data={"sub": user.get("username")}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signup", response_model=UserOutSchema)
async def create_new_user(
    userIn: UserInSchema, session: AsyncSession = Depends(db_session)
):
    # Verifica se o usuario ja existe
    user_service = UserService(session=session)
    user = await user_service.check_user(userIn)
    if user:
        raise HTTPException(
            status_code=409,
            detail="Username and/or e-mail already exists",
        )
    new_user = User(
        username=userIn.username,
        email=userIn.email,
        full_name=userIn.full_name,
        hashed_password=await user_service.get_password_hash(userIn.password),
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


@router.get("/users/me/", response_model=UserOutSchema)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
