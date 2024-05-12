from calendar import weekday
import asyncio
from datetime import datetime, timedelta
from func_cache.cache import currentday_dict



class CurrentDay:
    def __init__(self, plus_day: int=0):
        self.year = datetime.now().year
        self.month = datetime.now().month
        self.day = datetime.now().day
        self.plus_day = plus_day

    async def today_day_week(self): 
        return weekday(self.year, self.month, self.day) 
    
    async def tomorrows_day_week(self):
        day_of_the_week = weekday(self.year, self.month, self.day)
        return day_of_the_week+1

async def current_day_one(numday):
    result = currentday_dict[numday]
    return f'{result}_one'

async def current_day_two(numday):
    result = currentday_dict[numday]
    return f'{result}_two'

# current_day = CurrentDay()
# print(asyncio.run(current_day.tomorrows_day_week()))