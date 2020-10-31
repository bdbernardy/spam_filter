import os
from dotenv import load_dotenv
from app.core.wsl2_host import get_host

load_dotenv()

USE_LOCAL_WSL2 = os.getenv("USE_LOCAL_WSL2")
MONGO_CONNECTION_STRING = os.getenv("MONGO_CONNECTION_STRING")

if USE_LOCAL_WSL2:
    host_ip = get_host()
    MONGO_CONNECTION_STRING = MONGO_CONNECTION_STRING.replace("WSL_HOST", host_ip)
