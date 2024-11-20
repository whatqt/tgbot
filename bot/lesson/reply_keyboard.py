from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types



async def butons(message: types.Message, numbering):
    builder = ReplyKeyboardBuilder() 
    builder.add(types.KeyboardButton(text=f'Понедельник {numbering} недели')),
    builder.add(types.KeyboardButton(text=f'Вторник {numbering} недели')),
    builder.add(types.KeyboardButton(text=f'Среда {numbering} недели')),
    builder.add(types.KeyboardButton(text=f'Четверг {numbering} недели')),
    builder.add(types.KeyboardButton(text=f'Пятница {numbering} недели')),
    builder.add(types.KeyboardButton(text=f'Суббота {numbering} недели')),
    builder.add(types.KeyboardButton(text=f'Вернуться назад'))
    builder.adjust(3)
    await message.reply('Выберите день недели', reply_markup=builder.as_markup())

async def schedule_class(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Расписание первой недели'))
    builder.add(types.KeyboardButton(text='Расписание второй недели'))
    builder.add(types.KeyboardButton(text='Вернуться в главное меню'))
    builder.adjust(2)
    await message.reply('Выберите неделю', reply_markup=builder.as_markup(resize_keyboard=True))
