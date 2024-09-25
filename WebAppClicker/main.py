import sys
sys.path.append('..')
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Response, Body
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db.function import *
from asyncio import sleep
from bot.clicker.cookie_user_webapp import cookie_user



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

@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket, 
    response: Response,
    id_user):

    await websocket.accept()
    print('connect')
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        print("Disconnect")

    
@app.post("/update_data")
async def create_cookie(data = Body()):
    id_user = data['id_user']
    clicks = data['clicks']
    await update_clicks(id_user, clicks)
    print('update data completed successfully')
