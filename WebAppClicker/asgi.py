import sys
sys.path.append('..')
from fastapi import FastAPI, \
    Request, Response, Body, Cookie
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.function import *
from static.data.data_users import *
import asyncio
import json
import aiofiles
from data_json.entity_explore_parametrs_from_lvl import data_entity_explore_lvl




app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates")
 

@app.get("/")
async def index(request: Request, id_user: int, username):
    print(id_user)
    await create_user_info(id_user, username)
    data = await get_info_data_users(id_user)
    
    print(data)
    context = {
        "id_user": data[0], 
        "username": data[1],
        "quantity_explore_entity": data[2], 
        "quantity_logistics_entity": data[3], 
        "quantity_gold": data[4],
        "quantity_token": data[5]  
    }
    html = templates.TemplateResponse(request, "index.html", context)
    return html

@app.get("/send_entity_in_raid")
async def site_send_entity(request: Request, id_user: int):
    data_user = await get_info_data_users(id_user)
    print(data_user)
    if data_user:
        # два варианта: использовать aiofiles или же просто хранить данные в файле py
        data_lvl = await get_info_lvl_users(id_user)
        context = {
            "id_user": data_user[0], 
            "username": data_user[1],
            "quantity_gold": data_user[4],
            "quantity_token": data_user[5],
            "time_raid": data_entity_explore_lvl[data_lvl[1]]["time_raid"],
            "golds": data_entity_explore_lvl[data_lvl[1]]["gold_from_raid"],
            "tokens": data_entity_explore_lvl[data_lvl[1]]["token_from_raid"],
        }

        return templates.TemplateResponse(
            request, 
            "send_entity_in_raid.html", 
            context
        )
    else: 
        return HTMLResponse("Error", status_code=506)

@app.post("/end_time_raid")
async def end_time_raid(data = Body()):
    print(data)


@app.get("/favicon.ico")
async def favicon(request: Request):
    pass


# функция для отправки entity в raid. После рейда они прнесут gold в размере 50gold на 1 entity а все 3 entiry будут приносить 0.1 token. 
# В бд заносятся данные кол-во entity и время нажатия кнопки. Забрать награду можно будет через два часа. 
# В Html сделать так, чтоб был отсчёт (00:02:03, 02 и т.д)

# сделать что-то типа clash of clans: со своей ратушой; два вида entity: ученые и иследовательские; 
# иследовательские отрпавляются в raid чтоб находить ратуши других игроков и по окончанию raid'а пользователь получает награду
# иследовательские entity так же смогут находить различние плюшки по пути: от камня на котором будет промокод, 
# до сложного шифра, который придётся разгадывать чтоб получить награду
# чем выше уровень entity чем больше и интересней награды они находят
# полученные плюшки будут храниться в отдельной вкладке
# мб задания будут связаны с курсорм пользователя, но это не точно. 

# ученые entity будут развивать инфраструктуру ратуши позволяя пользователю в дальнейшем улучшать entity в разных аспектах: скорость, добыча, наход плюшек и т.д
# будут приносить схемы для улучшения и новые здания