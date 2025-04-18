# from main import BOT
from dotenv import load_dotenv
import os
from aiogram import Bot
import asyncio
import logging


load_dotenv()
BOT = Bot(token=os.getenv('TOKEN_BOT'))

class LogBase:
    bot: Bot = BOT
    log_chats = {
        "create_or_update_user": -4685065356,
        "cache_update": -4112086004,
        "error": -4758269339,
        "statistics": None, # заглушка
    }

class CustomErrorHandler(logging.Handler):
    def emit(self, record):
        if record.levelname == "ERROR":
            bot = LogBase.bot
            chat = LogBase.log_chats["error"]
            asyncio.create_task(
                bot.send_message(chat, record.message)
            )

