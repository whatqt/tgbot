from aiogram import Router, F
from aiogram.filters import Command,  CommandObject
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from parser.parser import *
# from data_base.db import insert_all
from os import system



router = Router()


@router.message(Command('admin'))
async def admin(message: types.Message):
    if message.from_user.id == 1752086646:
        await message.reply(f'''
/ver - посмотреть id чата\n
/system <agrs> - выполняет системную команду cmd
/while_time - запускает команду на проверку недели
/update_task - после падения сервера возобновляет уведомления
''')
    else:pass

@router.message(Command('ver'))
async def ver(message: types.Message):
    await message.answer(f'id чата: {message.chat.id}')

@router.message(Command('system'))
async def off(message: types.Message, command: CommandObject):
    if message.from_user.id == 1752086646:
        if command.args is None:
            await message.reply('Передайте команду')
            return
        
        result = system((command.args))
        await message.reply(f'Команда {str(command.args)} успешно выполнена.\n{result}')

    else:pass