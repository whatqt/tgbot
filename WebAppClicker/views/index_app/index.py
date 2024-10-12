import sys
sys.path.append('..')
from fastapi import FastAPI, Request 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db.function import create_user_info, get_info_data_users




app1 = FastAPI()
app1.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates")
 

@app1.get("/")
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
 
@app1.get("/favicon.ico")
async def favicon(request: Request):
    pass

# @app1.get("/")
# async def favicon(request: Request):
#     return {"Message" : "ЕБАТЬ ОНО РАБОТАЕТ"}
