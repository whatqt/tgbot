from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram import types
from aiogram import Bot
import os
from postgresql.management.manage_send_mess.manage_mess_by_time import \
    ManageSendMessTime
from dotenv import load_dotenv
import asyncio
from asyncio import CancelledError
from .logic.main_func import send_mess_by_time





load_dotenv()
router = Router()
users_use_notification = {}

bot = Bot(token=os.getenv('TOKEN_BOT'))

@router.message(Command("send_class_by_time"))
async def view_send_class_by_time(
    message: types.Message,
    command: CommandObject
    ):
    task = asyncio.create_task(
        send_mess_by_time(
            message,
            command,
        )
    )
    if message.from_user.id not in users_use_notification:
        users_use_notification[message.from_user.id] = task
    try:
        print("Задача запущена")
        await task
    except CancelledError:
        print("Задача отменена")
        manage_send_mess_time = ManageSendMessTime(
            message.from_user.id
        )
        await manage_send_mess_time.delete_time()
        del users_use_notification[message.from_user.id]
        print("Данные удалены")

@router.callback_query(F.data == 'edit')
async def edit(callback: types.CallbackQuery):
    task = users_use_notification[callback.from_user.id]
    print(task)
    task.cancel()
    await callback.message.edit_text(
        "Используйте ещё раз комманду /send_class_by_time"
    )
    await callback.answer()
