from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from aiogram import Bot
import os
from dotenv import load_dotenv
from aiogram.types import FSInputFile
import logging
import asyncio



load_dotenv()
router = Router()

bot = Bot(token=os.getenv('TOKEN_BOT'))


@router.message(Command("logs"))
async def logs(message: types.Message):
    if message.from_user.id == 1752086646:
        file_logs = FSInputFile("logs.log")
        await message.answer_document(file_logs)
        print("Команда logs выполнена")

async def send_file(file):  
    await bot.send_document(
        -4685168406,
        file
    )

class CustomErrorHandler(logging.Handler):
    def emit(self, record):
        if record.levelname == "ERROR":
            file_logs = FSInputFile("logs.log")
            try:
                asyncio.create_task(
                    send_file(
                        file_logs
                    )
                )
            except RuntimeError:
                pass
                print("ошибка в логах")


