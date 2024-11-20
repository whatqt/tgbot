from calendar import weekday
from datetime import datetime



currentday_dict = {
    0: 'monday',
    1: 'tuesday',
    2: 'wednesday',
    3: 'thursday',
    4: 'friday',
    5: 'saturday',
    6: None
}

class CurrentDay:
    def __init__(self):
        self.year = datetime.now().year
        self.month = datetime.now().month
        self.day = datetime.now().day

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

