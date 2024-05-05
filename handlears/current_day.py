from calendar import weekday
import asyncio
from datetime import datetime, timedelta
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

async def current_day_two(numday):
    result = currentday_dict[numday]
    return f'{result}_two'

