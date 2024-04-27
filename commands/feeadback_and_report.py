from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram import types
import asyncio
from aiogram import Bot



router = Router()
bot = Bot('6573990032:AAGRALx8BGzMNIj1KulH8A_onrv6mKLENEw')


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
    
    feedback = command.args
    await bot.send_message(
    -4149670794,
    f'#отзыв\nПоступил отзыв от @{message.from_user.username}\nid пользователя: {message.from_user.id}\nОтзыв: {feedback}'                  
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
    -4149670794,
    f'#ошибка\nПоступил report от @{message.from_user.username}\nid пользователя: {message.from_user.id}\nОшибка: {command.args}'  
        )
    
    await message.reply((f'Спасибо что сообщили об ошибке, @{message.from_user.username}!'))
