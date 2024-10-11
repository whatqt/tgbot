import sys
sys.path.append('..')
from fastapi import FastAPI, WebSocket, WebSocketDisconnect\
    ,Request, Response, Body
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db.function import *
from static.data.data_users import *
import asyncio



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates")
 

@app.get("/")
async def read_root(request: Request, id_user):
    print(id_user)
    clicks = await get_data(id_user)
    print(clicks)
    return templates.TemplateResponse(request, "index.html")

async def update_data_db(id_user, clicks):
    pass

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