import sys
sys.path.append('..')
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from views.index_app.index import app1
from views.entity_explore_app.entity_explore import app2



app = FastAPI()
app.mount("/entity_explore", app2)
app.mount("/", app1)
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates")
















# 12.10.2024 доделать механику отправки explore entity в raid. (Улучшение, плюшки и т.д)
# функция для отправки entity в raid. После рейда они прнесут gold в размере 50gold на 1 entity а все 3 entiry будут приносить 0.1 token. 
# В бд заносятся данные кол-во entity и время нажатия кнопки. Забрать награду можно будет через два часа. 
# В Html сделать так, чтоб был отсчёт (00:02:03, 02 и т.д)

# сделать что-то типа clash of clans: со своей инфраструктурой; два вида entity: ученые и иследовательские; 
# иследовательские entity так же смогут находить различние плюшки по пути: от камня на котором будет промокод, 
# до сложного шифра, который придётся разгадывать чтоб получить награду
# чем выше уровень entity чем больше и интересней награды они находят
# полученные плюшки будут храниться в отдельной вкладке
# мб задания будут связаны с курсорм пользователя, но это не точно. 

# ученые entity будут связаны с инфраструктурой 
# Инфраструктура будет выглядить как карта, где куча точек, которых можно будет прокачивать 

# инфраструктура будет отвечать за качество иследовательских entity.
# Под "качеством" подразумевается следующие параметры: добавление минимального и максимального значения нагарды для gold и token (Появляется рандом)
# 
# Так же появится раздел с прокачкой entity в находке. Они смогут находить "плюшки". По началу это будет не доступно
#
# Уме
