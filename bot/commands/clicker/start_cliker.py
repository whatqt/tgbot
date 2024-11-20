import sys
sys.path.append('..')
from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from WebAppClicker.db.connect import create_connection
from asyncpg.exceptions import UniqueViolationError



router = Router()



def create_keyboard(id_user, username) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Play clicker",
        web_app=types.WebAppInfo(
            url=f'https://e31a-146-158-112-164.ngrok-free.app/?id_user={id_user}&username={username}'
        )
    ))
    return builder.as_markup()

#мб использовать вебхук
@router.message(Command("clicker"))
async def start_clicker(message: types.Message):
    if message.from_user.id == 1752086646:
        await message.answer('Кликер...', reply_markup=create_keyboard(
            message.from_user.id,
            message.from_user.username
            )
        )

    