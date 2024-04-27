from calendar import weekday
import asyncio
from datetime import datetime
from func_cache.cache import currentday_dict



class CurrentDay:
    def __init__(self):
        self.year = datetime.now().year
        self.month = datetime.now().month
        self.day = datetime.now().day

    async def __call__(self): 
        return weekday(self.year, self.month, self.day)


async def current_day_one(numday):
    result = currentday_dict[numday]
    return f'{result}_one'
    #так как решение с двумя функциями (и соответственно с двумя кнопка) не очень
    #то в воскресенье нужно будет написать функцию, которая будет иметь следующий функционал
    #если будет первая неделя, то возращаться будет 0, если же вторая неделя, то 1
    #сами дни недели придётся отслеживать и писать логику придётся вручную, ибо на сайте нет никаких указателей.

async def current_day_two(numday):
    result = currentday_dict[numday]
    return f'{result}_two'


    #оч крутая идея. Можно создать функцию, которая будет обновлять значение каждые 24 часов (сменился день, сменился и счётчик)
    #При достижение определенного значения (6 функция вернёт True и будет показывать вторую неделю, за место первой
    #При этом, кнопка будет одна

