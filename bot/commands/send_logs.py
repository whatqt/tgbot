from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from aiogram import Bot
import os
from dotenv import load_dotenv
from aiogram.types import FSInputFile
from logic_logs.file.logger import logger



load_dotenv()
router = Router()

bot = Bot(token=os.getenv('TOKEN_BOT'))


@router.message(Command("logs"))
async def logs(message: types.Message):
    if message.from_user.id == 1752086646:
        logger.info("Команда logs выполняется...")
        file_logs = FSInputFile("logs/RII_BOT.log")
        await message.answer_document(file_logs)
        logger.info("Команда logs выполнена")

async def send_file(file):  
    await bot.send_document(
        -4758269339,
        file
    )




