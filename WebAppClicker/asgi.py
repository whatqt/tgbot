import sys
sys.path.append('..')
from fastapi import FastAPI, BackgroundTasks, \
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
from data_json.is_activated_raid import users_of_the_activated_raid
from views.index_app.index import app1
from views.entity_explore_app.entity_explore import app2
from app_two import app_two


app = FastAPI()
app.mount("/", app1)
app.mount("/", app2)
# app.mount("/", app_two)
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates")


# app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"))
# templates = Jinja2Templates(directory="templates")
 

# @app.get("/")
# async def index(request: Request, id_user: int, username):
#     print(id_user)
#     await create_user_info(id_user, username)
#     data = await get_info_data_users(id_user)
    
#     print(data)
#     context = {
#         "id_user": data[0], 
#         "username": data[1],
#         "quantity_explore_entity": data[2], 
#         "quantity_logistics_entity": data[3], 
#         "quantity_gold": data[4],
#         "quantity_token": data[5]  
#     }
#     html = templates.TemplateResponse(request, "index.html", context)
#     return html

# @app.get("/send_entity_in_raid")
# async def site_send_entity(request: Request, id_user: int):
#     data_user = await get_info_data_users(id_user)
#     print(data_user)
#     if data_user:
#         # два варианта: использовать aiofiles или же просто хранить данные в файле py
#         data_lvl = await get_info_lvl_users(id_user)
#         context = {
#             "id_user": data_user[0], 
#             "username": data_user[1],
#             "quantity_gold": data_user[4],
#             "quantity_token": data_user[5],
#             "time_raid_in_hour": data_entity_explore_lvl[data_lvl[1]]["time_raid_in_hour"],
#             "time_raid_in_minute": data_entity_explore_lvl[data_lvl[1]]["time_raid_in_minute"],
#             "golds": data_entity_explore_lvl[data_lvl[1]]["reward_in_gold"],
#             "tokens": data_entity_explore_lvl[data_lvl[1]]["reward_in_token"], 
#             "users_of_the_activated_raid": users_of_the_activated_raid
#         }

#         return templates.TemplateResponse(
#             request, 
#             "send_entity_in_raid.html", 
#             context
#         )
#     else: 
#         return HTMLResponse("Error", status_code=506)

# async def create_task_active_raid(
#         id_user, reward_in_gold, 
#         reward_in_token, time_end_raid
#     ):

#     await insert_data_of_active_raid(
#         id_user, reward_in_gold, 
#         reward_in_token, time_end_raid
#     )
#     await asyncio.sleep(60)
#     await update_golds_tokens(id_user, reward_in_gold, reward_in_token)
#     await delete_data_of_active_raid(id_user)
#     print(users_of_the_activated_raid)
#     users_of_the_activated_raid.remove(id_user)
#     print("Задача выполнилась")
#     # сделайть рандомную выдачу плюшек при помощи модуля random


# @app.post("/end_time_raid")
# async def end_time_raid(background_tasks: BackgroundTasks, data = Body()):
#     print(data)
#     users_of_the_activated_raid.append(data["id_user"])
#     print(users_of_the_activated_raid)
#     background_tasks.add_task(create_task_active_raid, data["id_user"], data["golds"], data["tokens"], data["time"])
#     print('Задача установлена')

# @app.get("/favicon.ico")
# async def favicon(request: Request):
#     pass






# 12.10.2024 доделать механику отправки explore entity в raid. (Улучшение, плюшки и т.д)
# функция для отправки entity в raid. После рейда они прнесут gold в размере 50gold на 1 entity а все 3 entiry будут приносить 0.1 token. 
# В бд заносятся данные кол-во entity и время нажатия кнопки. Забрать награду можно будет через два часа. 
# В Html сделать так, чтоб был отсчёт (00:02:03, 02 и т.д)

# сделать что-то типа clash of clans: со своей ратушой; два вида entity: ученые и иследовательские; 
# иследовательские entity так же смогут находить различние плюшки по пути: от камня на котором будет промокод, 
# до сложного шифра, который придётся разгадывать чтоб получить награду
# чем выше уровень entity чем больше и интересней награды они находят
# полученные плюшки будут храниться в отдельной вкладке
# мб задания будут связаны с курсорм пользователя, но это не точно. 

# ученые entity будут развивать инфраструктуру ратуши позволяя пользователю в дальнейшем улучшать entity в разных аспектах: скорость, добыча, наход плюшек и т.д
# будут приносить схемы для улучшения и новые здания