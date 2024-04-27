from aiogram import Router, F
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from postgresql.db import *
from func_cache.check_cache import *
import asyncio 
from keyboard_builder.reply_keyboard import *
from handlears.current_day import *
from handlears.score_week import *



router = Router()


async def use_for(method, list): 
    numbers_couple = 0
    line = ''
    time = {1: '8:30-10:00', 2: '10:10-11:40', 3: '12:10-13:40', 4: '13:50-15:20', 5: '15:30-17:00'}
    for day in list:
        numbers_couple+=1
        if day == '':
            line += (f'{time[numbers_couple]} | {numbers_couple} пара | окно\n\n')
        else:
            line += (f'{time[numbers_couple]} | {numbers_couple} пара | {day}\n\n')  
    await method(line)
    list.clear()

async def display_the_schedule(id_user, method, day):
    try:
        id_group = await check_id_group(id_user)
        end_list = await check(id_group, day, 1)
        await use_for(method, end_list.copy())
    except AttributeError:
        await method('❌ Выберите пожалуйста группу при помощи команды /group')

@router.message(F.text == 'Расписание занятий')
async def schedule(message: types.Message):
    await schedule_class(message)

@router.message(F.text == 'Расписание первой недели')
async def await_button(message: types.Message):
    await butons(message, 'первой')
    
@router.message(F.text == 'Расписание второй недели')
async def await_button(message: types.Message):
    await butons(message, 'второй')

@router.message(F.text == 'Вернуться в главное меню')
async def back_menu(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Сегодняшние пары'))
    builder.add(types.KeyboardButton(text='Расписание занятий'))
    builder.adjust(2)
    await message.answer('Вы вернулись в главное меню.',reply_markup=builder.as_markup(resize_keyboard=True))

@router.message(F.text == 'Вернуться назад')
async def back_keyboard(message: types.Message):
    await schedule_class(message)

@router.message(F.text == 'Понедельник первой недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message.answer, 'monday_one')

@router.message(F.text == 'Вторник первой недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message.answer, 'tuesday_one')

@router.message(F.text == 'Среда первой недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message.answer,'wednesday_one')

@router.message(F.text == 'Четверг первой недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message.answer, 'thursday_one')

@router.message(F.text == 'Пятница первой недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message.answer, 'friday_one')

@router.message(F.text == 'Суббота первой недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message.answer, 'saturday_one')

@router.message(F.text == 'Понедельник второй недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message.answer, 'monday_two')

@router.message(F.text == 'Вторник второй недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message.answer, 'tuesday_two')

@router.message(F.text == 'Среда второй недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message.answer, 'wednesday_two')

@router.message(F.text == 'Четверг второй недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message.answer, 'thursday_two')

@router.message(F.text == 'Пятница второй недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message.answer, 'friday_two')

@router.message(F.text == 'Суббота второй недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message.answer, 'saturday_two')

@router.message(F.text == 'Сегодняшние пары')
async def otvet(message: types.Message):
    try:
        await display_the_schedule(message.from_user.id, message.answer, await chek_week())
    except KeyError:
        await message.answer('В воскресенье пар нет')
        
# @router.message(F.text == 'Сегодняшние пары второй недели')
# async def two_week(message: types.Message):
#     current_day = CurrentDay()
#     try:
#         await display_the_schedule(message.from_user.id, message.answer, await current_day_two(await current_day()))
#     except KeyError:
#         await message.answer('В воскресенье пар нет')


