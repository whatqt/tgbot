from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder



router = Router()

@router.message(Command('schedule'))
async def schedule(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Сегодняшние пары'))
    builder.add(types.KeyboardButton(text='Завтрашние пары'))
    builder.add(types.KeyboardButton(text='Расписание занятий'))
    builder.adjust(3)
    await message.reply(
    'Вы создали главное меню. Выберите функцию при помощи нажатия на кнопку.',
    reply_markup=builder.as_markup(resize_keyboard=True))

async def create_schedule(callback: types.CallbackQuery):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Сегодняшние пары'))
    builder.add(types.KeyboardButton(text='Завтрашние пары'))
    builder.add(types.KeyboardButton(text='Расписание занятий'))
    builder.adjust(3)
    return await callback.message.reply('Вы создали главное меню. Выберите функцию при помощи нажатия на кнопку.', reply_markup=builder.as_markup(resize_keyboard=True))