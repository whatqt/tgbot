import sys
sys.path.append('..')
from fastapi import FastAPI, Request 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db.function import create_user_info, get_info_data_users



app_two = FastAPI()

@app_two.get("/")
async def favicon():
    return {"Message" : "ЕБАТЬ ОНО РАБОТАЕТ"}