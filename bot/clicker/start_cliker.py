from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from WebAppClicker.db.connect import create_connection
from asyncpg.exceptions import UniqueViolationError
from .cookie_user_webapp import cookie_user

router = Router()



def create_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Play clicker",
        web_app=types.WebAppInfo(
            url='https://ca97-178-186-121-171.ngrok-free.app'
        )
    ))

    return builder.as_markup()


@router.message(Command("clicker"))
async def start_clicker(message: types.Message):
    try:
        cursor = await create_connection()
        await cursor.execute(f"INSERT INTO data_user VALUES ({message.from_user.id}, '{message.from_user.username}', 0)")    
    except UniqueViolationError: pass
    finally: 
        await cursor.close()
    await message.answer('Кликер...', reply_markup=create_keyboard())