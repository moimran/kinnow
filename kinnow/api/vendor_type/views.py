from fastapi import APIRouter
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json




router = APIRouter()

@router.get("/vendors")
async def get_vendors(request: Request):
    dev_obj = request.app.state.device_types
    print(dev_obj[30].get('interfaces'))
    # convert dictionary to json
    return JSONResponse(content=dev_obj[30].get('interfaces'))