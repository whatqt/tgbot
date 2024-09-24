from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Response
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db.connect import create_connection
from asyncio import sleep


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
 

@app.get("/")
async def read_root(requests: Request, response: Response):
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    print(requests.scope)
    return templates.TemplateResponse(requests, "index.html", {"test": "testtt"})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, response: Response):
    print(websocket.scope)
    await websocket.accept()
    print('connect')
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        print("Disconnect")

    
@app.get("/cookie")
def create_cookie(request: Request, response: Response):
    return templates.TemplateResponse(request, "index.html", {"test": "testtt"})

