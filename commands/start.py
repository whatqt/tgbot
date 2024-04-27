from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types



router = Router()

@router.message(Command('start'))
async def start_button(message: types.Message):
    await message.answer(f'Привет @{message.from_user.username}. Нажми на /help чтобы посмотреть доступные команды.')