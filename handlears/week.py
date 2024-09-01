from aiogram import Router, F
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from postgresql.db import *
from func_cache.check_cache import *
from keyboard_builder.reply_keyboard import *
from handlears.current_day import CurrentDay
from handlears.score_week import *
from aiogram.filters import Command


router = Router()
bot = Bot(token="6573990032:AAGRALx8BGzMNIj1KulH8A_onrv6mKLENEw")

def emoji_number_couple(nubmer: int):
    match nubmer:
        case 1:
            return '1️⃣'
        case 2:
            return '2️⃣'
        case 3:
            return '3️⃣'
        case 4:
            return '4️⃣'
        case 5:
            return '5️⃣'
        
        case _:
            return nubmer
ttt = '341 ауд. Информатика лек Кнышов И.Ю. ассистент'

def edited_numbers_cabinet(text: str):
    numbers_cabinet = text.split('.', 1)


def emoji_time_couple(time: str):
    match time:
        case '8:30-10:00':
            return '🕗'
        case '10:10-11:40':
            return '🕙'
        case '12:10-13:40':
            return '🕛'
        case '13:50-15:20':
            return '🕐'
        case '15:30-17:00':
            return '🕜'
        

async def use_for(message: types.Message, list, id_user, method): 
    numbers_couple = 0
    line = ''
    time = {1: '8:30-10:00', 2: '10:10-11:40', 3: '12:10-13:40', 4: '13:50-15:20', 5: '15:30-17:00'}
    for day in list:
        numbers_couple+=1
        if day == '':
            line += (f'{emoji_time_couple(time[numbers_couple])} <b>{time[numbers_couple]}</b> | {emoji_number_couple(numbers_couple)} пара | <i><b>Окно</b></i>\n\n')
        else:
            day = day.split('.', 1)
            line += (f'{emoji_time_couple(time[numbers_couple])} <b>{time[numbers_couple]}</b> | {emoji_number_couple(numbers_couple)} пара | <b><u>{day[0]}</u></b>{day[1]}\n\n')  
    match method:
        case 'answer':
            await message.reply(line, parse_mode='HTML')
        case 'bot_send':
            await bot.send_message(id_user, line, parse_mode='HTML')
        case 'text':
            return line
    # list.clear()


async def display_the_schedule(id_user, message: types.Message, day, method):
    try:
        id_group = await check_id_group(id_user)
        end_list = await check(id_group, day, 1)
        match method:
            case 'text':
                info = await use_for(message, end_list.copy(), id_user, method)
                return info
            case _:
                await use_for(message, end_list.copy(), id_user, method)

    except AttributeError:
        match method:
            case 'answer':
                await message.reply('❌ Выберите пожалуйста группу при помощи команды /group')
            case 'bot_send':
                await bot.send_message(id_user, '❌ Выберите пожалуйста группу при помощи команды /group')

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
    builder.add(types.KeyboardButton(text='Завтрашние пары'))
    builder.add(types.KeyboardButton(text='Расписание занятий'))
    builder.adjust(2)
    await message.answer('Вы вернулись в главное меню.',reply_markup=builder.as_markup(resize_keyboard=True))

@router.message(F.text == 'Вернуться назад')
async def back_keyboard(message: types.Message):
    await schedule_class(message)

@router.message(F.text == 'Понедельник первой недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message, 'monday_one', 'answer')

@router.message(F.text == 'Вторник первой недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message, 'tuesday_one', 'answer')

@router.message(F.text == 'Среда первой недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message,'wednesday_one', 'answer')

@router.message(F.text == 'Четверг первой недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message, 'thursday_one', 'answer')

@router.message(F.text == 'Пятница первой недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message, 'friday_one', 'answer')

@router.message(F.text == 'Суббота первой недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message, 'saturday_one', 'answer')

@router.message(F.text == 'Понедельник второй недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message, 'monday_two', 'answer')

@router.message(F.text == 'Вторник второй недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message, 'tuesday_two', 'answer')

@router.message(F.text == 'Среда второй недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message, 'wednesday_two', 'answer')

@router.message(F.text == 'Четверг второй недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message, 'thursday_two', 'answer')

@router.message(F.text == 'Пятница второй недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message, 'friday_two', 'answer')

@router.message(F.text == 'Суббота второй недели')
async def otvet(message: types.Message):
    await display_the_schedule(message.from_user.id, message, 'saturday_two', 'answer')

@router.message(F.text == 'Сегодняшние пары')
async def otvet(message: types.Message):
    try:
        current_day = CurrentDay()
        info_class = await display_the_schedule(
            message.from_user.id, message,  
            await check_week(await current_day.today_day_week()), 'text'
        )
        if info_class is None:
            await message.answer('❌ Выберите пожалуйста группу при помощи команды /group')
            
        else:
            info_week = await week()
            await message.answer(f'{info_week}\n\n{info_class}', parse_mode="HTML")

    except KeyError:
        info_week = await week()
        await message.answer(f'{info_week}\n\nВ воскресенье пар нет!')
        
@router.message(Command('while_time'))
async def time_while(message: types.Message):
    if message.from_user.id == 1752086646:
        await while_time()

@router.message(F.text == 'Завтрашние пары')
async def tomorrow_class(message: types.Message):
    try:
        current_day = CurrentDay()
        if await current_day.today_day_week() == 6:
            info_class = await display_the_schedule(
                    message.from_user.id, message, 
                    await check_week(input_score_week=True), 'text'
                )
            if info_class is None:
                await message.answer('❌ Выберите пожалуйста группу при помощи команды /group')
                return
            else:
                info_week = await week(input_score_week=True)
                await message.answer(f'{info_week}\n\n{info_class}', parse_mode='HTML')
                return
            
        info_class = await display_the_schedule(
            message.from_user.id, message, 
            await check_week(await current_day.tomorrows_day_week()), 'text'
        )
        if info_class is None:
            await message.answer('❌ Выберите пожалуйста группу при помощи команды /group')
            
        else:
            info_week = await week()
            await message.answer(f'{info_week}\n\n{info_class}', parse_mode='HTML')

    except KeyError:
        info_week = await week()
        await message.answer(f'{info_week}\n\nВ воскресенье пар нет!')
    



