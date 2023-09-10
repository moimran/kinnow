from api.router import api_router
from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from kinnow.repo import DTLRepo
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(application: FastAPI):
    repo = DTLRepo()
    files, vendors = repo.get_devices(repo.get_devices_path())
    device_types = repo.parse_files(files)
    print("Helloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
    application.state.device_types = device_types
    yield


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """

    app = FastAPI(
        title="KINNOW",
        description="gui based network deployment tool",
        version="1.0",
        docs_url="/api/docs/",
        redoc_url="/api/redoc/",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
        lifespan=lifespan,
    )

    app.include_router(router=api_router, prefix="/api")

    return app
