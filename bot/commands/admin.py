from aiogram import Router, F
from aiogram.filters import Command,  CommandObject
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from os import system



router = Router()


@router.message(Command('admin'))
async def admin(message: types.Message):
    if message.from_user.id == 1752086646:
        await message.reply(f'''
/ver - посмотреть id чата\n
/cache - обновление кэша расписания
/cache_group_users - обновление кэша пользователей у которых есть группы
/while_time - запускает команду на проверку недели
/send_info_update - отправка пользователям сообщения об обновлении/запуске бота
/all_notification - показывает все активные уведомления
/activation_notification <id_user> - возобновляет уведомление из кэша
''')
    else:pass

@router.message(Command('ver'))
async def ver(message: types.Message):
    await message.answer(f'id чата: {message.chat.id}')
