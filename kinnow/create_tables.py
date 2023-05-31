from sqlmodel import create_engine
from db.models.system_user import SystemUser
from db.models.device_account import DeviceAccount
from db.models.user import User
from db.models.device import Device
    

sqlite_url = f"postgresql://kinnow:kinnow@192.168.232.129:5432/kinnow"

engine = create_engine(sqlite_url, echo='debug')

DeviceAccount.metadata.create_all(engine, checkfirst=True)
Device.metadata.create_all(engine, checkfirst=True)
User.metadata.create_all(engine, checkfirst=True)
