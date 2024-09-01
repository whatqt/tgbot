from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram import types
from aiogram import Bot
import os
from postgresql.db import get_id_users
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder




router = Router()
bot = Bot(token=os.getenv('TOKEN_BOT'))
class Form(StatesGroup): 
    mesg_update = State()


@router.message(Command('send_info_update'))
async def send_info_update(message: types.Message, state: FSMContext):
    if message.from_user.id == 1752086646:
        await state.set_state(Form.mesg_update)
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text='Прервать обновление',
            callback_data='cancel_update'
        ))

    await message.answer(
        'Напишите ниже своё объявление, которое будет отправлено всем участникам',
        reply_markup=builder.as_markup()
        )

@router.message(Form.mesg_update)
async def message_send(message: types.Message, state: FSMContext):
    if message.from_user.id == 1752086646:
        await state.update_data(mesg_update=message.text)
        user_data = await state.get_data()
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Да",
            callback_data='yes'
        ))
        builder.add(types.InlineKeyboardButton(
            text="Нет",
            callback_data='not'
        ))
        builder.add(types.InlineKeyboardButton(
            text="Прервать процесс",
            callback_data='cancel_update'
        ))
        await message.answer('Это окончательная версия?', reply_markup=builder.as_markup())

@router.callback_query(F.data == 'yes')
@router.message(Form.mesg_update)
async def update_yes(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == 1752086646:
        user_data = await state.get_data()
        id_users_list = await get_id_users()
        for id_user in id_users_list:
            print(id_user['id_user'])
            await bot.send_message(id_user['id_user'], user_data["mesg_update"])

        await state.clear()
        await callback.message.edit_text('Информация была успешно отправлена!')

@router.callback_query(F.data == 'not')
@router.message(Form.mesg_update)
async def update_not(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == 1752086646:
        await callback.message.edit_text('Измените текст и после этого отправьте его')
        await callback.answer()

@router.callback_query(F.data == 'cancel_update')
@router.message(Form.mesg_update)
async def cancel_update(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == 1752086646:
        current_state = await state.get_state()
        print(current_state)
        if current_state is None:
            return
        
        await state.clear()
        await callback.message.edit_text('Процесс приостановлен')
        await callback.answer()

