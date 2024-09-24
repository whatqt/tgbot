from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram import types
from aiogram import Bot
import os


router = Router()
bot = Bot(token=os.getenv('TOKEN_BOT'))

@router.message(Command('feedback'))
async def feedback_user(
    message: types.Message,
    command: CommandObject
    ):

    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы\nпример команды /feedback <Ваш отзыв>"
        )
        return
    
    await bot.send_message(
    -4102265926,
    f'#отзыв\nПоступил отзыв от @{message.from_user.username}\nid пользователя: {message.from_user.id}\nОтзыв: {command.args}'                  
    )
    await message.reply(f'Благодарю за отзыв, @{message.from_user.username}!')


@router.message(Command('report'))
async def report_user(
    message : types.Message,
    command: CommandObject
    ):
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы\nпример команды /report <Подробности об ошибки>"
        )
        return
    
    await bot.send_message(
    -4102265926,
    f'#ошибка\nПоступил report от @{message.from_user.username}\nid пользователя: {message.from_user.id}\nОшибка: {command.args}'  
        )
    
    await message.reply((f'Спасибо что сообщили об ошибке, @{message.from_user.username}!'))
