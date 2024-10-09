import sys
sys.path.append('..')
from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from WebAppClicker.db.connect import create_connection
from asyncpg.exceptions import UniqueViolationError



router = Router()



def create_keyboard(id_user) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Play clicker",
        web_app=types.WebAppInfo(
            url=f'https://78c8-146-158-112-164.ngrok-free.app/?id_user={id_user}'
        )
    ))
    return builder.as_markup()

#мб использовать вебхук
@router.message(Command("clicker"))
async def start_clicker(message: types.Message):
    if message.from_user.id == 1752086646:
        try:
            cursor = await create_connection()
            await cursor.execute(f"INSERT INTO data_user VALUES ({message.from_user.id}, '{message.from_user.username}', 0)")    
        except UniqueViolationError: pass
        finally: 
            await cursor.close()

        await message.answer('Кликер...', reply_markup=create_keyboard(message.from_user.id))

    