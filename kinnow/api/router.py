from fastapi.routing import APIRouter
from fastapi import Depends

from api.system_user.views import router as system_user_router
from api.device_account.views import router as device_account_router
from api.devices.views import router as device_router
from api.users.views import router as user_router



api_router = APIRouter()
api_router.include_router(system_user_router, prefix="/system_user", tags=["system_user"])
api_router.include_router(
    device_account_router, prefix="/device_account", tags=["device_account"]
)
api_router.include_router(device_router, prefix="/device", tags=["device"])
api_router.include_router(user_router, prefix="/auth", tags=["Authentication"])
