import sys
sys.path.append('..')
from fastapi import FastAPI, WebSocket, WebSocketDisconnect\
    ,Request, Response, Body, BackgroundTasks
# from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db.function import *
from bot.clicker.cookie_user_webapp import cookie_user
from static.data.data_users import *
import asyncio


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
 

@app.get("/")
async def read_root(request: Request, id_user):
    print(id_user)
    clicks = await get_clicks(id_user)
    context = {"id_user": id_user, "clicks": clicks}
    html = templates.TemplateResponse(request, "index.html", context)
    html.set_cookie("id_user", id_user)

    return html


@app.post('/update_data_json')
async def update_data_json(data = Body()):
    data_users[data["id_user"]] = data["clicks"]
    

async def update_data_db(id_user, clicks):
    user_id_update_data_db.append(id_user)
    await asyncio.sleep(10)
    await update_clicks(id_user, clicks)
    user_id_update_data_db.remove(id_user)
    print("Задава выполнилась")



@app.post("/run_background_tasks")
async def run(data = Body()):
    id_user = data['id_user']
    clicks = data['clicks']
    if id_user in user_id_update_data_db:
        name_task = tasks.get(id_user)
        del tasks[id_user]
        user_id_update_data_db.remove(id_user)
        name_task.cancel()
    task = asyncio.create_task(update_data_db(id_user, clicks))
    print(task)
    tasks[id_user] = task
    print(tasks)
    try:
        await asyncio.gather(task)
    except asyncio.exceptions.CancelledError: print("Задача отменена")



@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket, 
    response: Response,
    id_user: int):
    await websocket.accept()
    print('connect')
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        print("Disconnect")

    
@app.post("/update_data")
async def update_data(data = Body()):
    id_user = data['id_user']
    clicks = data['clicks']
    print(clicks)
    await update_clicks(id_user, clicks)
    print('update data completed successfully')

@app.get("/favicon.ico")
async def favicon(request: Request):
    pass