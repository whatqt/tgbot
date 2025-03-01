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
from .logic.main_func import send_mess_by_time, update_task, admin_send_class_by_time
from commands.send_mess_by_time.text import text_info
from pymongo.errors import DuplicateKeyError
from mongodb.send_mess_time.cache_send_mess_time import CacheSendMessTime
from cache_group_users.cache_group_user import CacheGroupUsers




load_dotenv()
router = Router()
users_use_notification = {}

bot = Bot(token=os.getenv('TOKEN_BOT'))

@router.message(Command("send_class_by_time"))
async def view_send_class_by_time(
    message: types.Message,
    command: CommandObject
    ):
    if command.args is None:
        await message.reply(
            text_info["none_args"]
        )
        return
    cache_group_users = CacheGroupUsers()
    if message.from_user.id not in cache_group_users.cache_group_users_dict:
        await message.reply(
            text_info["id_group_none"]
        )
        return
    
    task = asyncio.create_task(
        send_mess_by_time(
            message,
            command,
        )
    )
    if message.from_user.id not in users_use_notification:
        users_use_notification[message.from_user.id] = task
        print(task)
    try:
        print("Задача запущена")
        await task
    except (CancelledError, DuplicateKeyError) :
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
    print(users_use_notification)
    print(task)
    task.cancel()
    cache_send_mess_time = CacheSendMessTime(callback.from_user.id)
    await cache_send_mess_time.delete_user()
    await callback.message.edit_text(
        "Используйте ещё раз комманду /send_class_by_time"
    )
    await callback.answer()

@router.message(Command("activation_notification"))
async def view_update_task(
    message: types.Message,
    command: CommandObject
    ):
    id_user = command.args
    if message.from_user.id != 1752086646:
        return 
    
    if command.args is None:
        await message.answer("Введите id пользователя")
        return

    task = asyncio.create_task(
        update_task(
            message,
            int(id_user),
        )
    )

    if message.from_user.id not in users_use_notification:
        users_use_notification[message.from_user.id] = task

    try:
        print("Задача запущена")
        await message.reply(f"Задача у {id_user} была запущена")
        await task
    except (CancelledError, DuplicateKeyError) :
        print("Задача отменена")
        manage_send_mess_time = ManageSendMessTime(
            message.from_user.id
        )
        await manage_send_mess_time.delete_time()
        del users_use_notification[message.from_user.id]
        print("Данные удалены в обработчике 'update_task'")

@router.message(Command("all_notification"))
async def view_all_active_notification(
    message: types.Message
    ):
    if message.from_user.id != 1752086646:
        return 
    
    cache_send_mess_time = CacheSendMessTime(...)
    data = await cache_send_mess_time.all_active_notification()
    if data is None:
        await message.answer("Данных нет")
        return
    data_str = ""
    for info in data:
        data_str+=f"{info["_id"]} : {info["time"]}\n\n"
    await message.answer(data_str)

@router.message(Command("admin_send_class_by_time"))
async def view_admin_send_class_by_time(
    message: types.Message,
    command: CommandObject
    ):
    if message.from_user.id != 1752086646:
        return 
    print("Робит")
    task = asyncio.create_task(
        admin_send_class_by_time(
            message,
            command,
        )
    )
    print(users_use_notification)
    if command.args not in users_use_notification:
        users_use_notification[command.args] = task

    try:
        print("Задача запущена")
        await message.reply(f"Задача у {command.args} была запущена")
        await task
    except (CancelledError, DuplicateKeyError) :
        print("Задача отменена")
        manage_send_mess_time = ManageSendMessTime(
            command.args
        )
        await manage_send_mess_time.delete_time()
        del users_use_notification[command.args]
        print("Данные удалены")
        print("147 строка")








