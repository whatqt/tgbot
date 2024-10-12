import sys
sys.path.append('..')
from fastapi import FastAPI, BackgroundTasks, Request, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.function import *
import asyncio
from data_json.entity_explore_parametrs_from_lvl import *
from data_json.is_activated_raid import users_of_the_activated_raid



app2 = FastAPI()
app2.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates")



@app2.get("/send_entity_in_raid")
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
            "time_raid_in_hour": data_entity_explore_lvl[data_lvl[1]]["time_raid_in_hour"],
            "time_raid_in_minute": data_entity_explore_lvl[data_lvl[1]]["time_raid_in_minute"],
            "golds": data_entity_explore_lvl[data_lvl[1]]["reward_in_gold"],
            "tokens": data_entity_explore_lvl[data_lvl[1]]["reward_in_token"], 
            "users_of_the_activated_raid": users_of_the_activated_raid
        }

        return templates.TemplateResponse(
            request, 
            "send_entity_in_raid.html", 
            context
        )
    else: 
        return HTMLResponse("Error", status_code=506)

async def create_task_active_raid(
        id_user, reward_in_gold, 
        reward_in_token, time_end_raid
    ):

    await insert_data_of_active_raid(
        id_user, reward_in_gold, 
        reward_in_token, time_end_raid
    )
    await asyncio.sleep(60)
    await update_golds_tokens(id_user, reward_in_gold, reward_in_token)
    await delete_data_of_active_raid(id_user)
    print(users_of_the_activated_raid)
    users_of_the_activated_raid.remove(id_user)
    print("Задача выполнилась")
    # сделайть рандомную выдачу плюшек при помощи модуля random


@app2.post("/end_time_raid")
async def end_time_raid(background_tasks: BackgroundTasks, data = Body()):
    print(data)
    users_of_the_activated_raid.append(data["id_user"])
    print(users_of_the_activated_raid)
    background_tasks.add_task(create_task_active_raid, data["id_user"], data["golds"], data["tokens"], data["time"])
    print('Задача установлена')

@app2.get("/upgrade_explore_entity")
async def upgrade_explore_entity(request: Request, id_user):
    data_user = await get_info_data_users(id_user)
    if data_user:
        lvl_users = await get_info_lvl_users(id_user)
        print(lvl_users)
        context = {
            "id_user": data_user[0], 
            "username": data_user[1],
            "quantity_gold": data_user[4],
            "quantity_token": data_user[5],
            "current_lvl_explore_entity": lvl_users[1],
            "next_lvl_explore_entity": lvl_users[1]+1,
            "next_reward_in_golds": data_entity_explore_lvl[lvl_users[1]+1]["reward_in_gold"],
            "next_reward_in_tokens": data_entity_explore_lvl[lvl_users[1]+1]["reward_in_token"],
            "price_lvl_up": price_lvl_up[lvl_users[1]+1]
        }

        print(context)
        return templates.TemplateResponse(
            request, 
            "upgrade_entity_explore.html",
            context
        )
    
    else: 
        return HTMLResponse("Error", status_code=506)

@app2.post("/upgrade_entity_explore")
async def end_time_raid(data = Body()):
    lvl_user = data
    print(lvl_user)
    if data['quantity_gold'] < data['price_lvl_up']:
        return {"message": "error. quantity_gold < price_lvl_up"}
    
    await update_lvl_explore_entity(data['id_user'])
    await write_downs_golds(data['id_user'], data['price_lvl_up'])
    print("Данные обновились. Кол-во golds было изменено")
#добавить redirect для избежания ошибок
@app2.get("/favicon.ico")
async def favicon():
    pass