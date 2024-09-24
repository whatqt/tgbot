from aiogram import types
from postgresql.db import *



class Time:
    def __init__(self, set_time: str, user_id: int):  
        self.set_time = set_time # устанавливает время когда придет уведомление
        self.user_id = user_id

    async def insert_date_time(self):
        hour, minute = self.set_time.split(':')
        # date = (f'{hour}:{minute}')
        await insert_into_time(self.user_id, hour, minute)

