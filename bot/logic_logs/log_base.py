# from main import BOT
from dotenv import load_dotenv
import os
from aiogram import Bot


load_dotenv()
BOT = Bot(token=os.getenv('TOKEN_BOT'))

class LogBase:
    def __init__(self):
        self.bot = BOT
        self.log_chats = {
            "create_or_update_user": -4685065356,
            "cache_update": -4112086004,
            "statistics": None, # заглушка
        }
