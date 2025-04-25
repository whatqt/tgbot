from aiogram import Router, F, Bot
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from cache_group_users.cache_group_user import CacheGroupUsers
from commands.cache_update.tools.check_cache import check
from ..reply_keyboard import schedule_class, butons
from ..current_day import CurrentDay
from ..score_week import *
from aiogram.filters import Command
from dotenv import load_dotenv
import os



load_dotenv()
router = Router()
bot = Bot(token=os.getenv("TOKEN_BOT"))

def emoji_number_couple(nubmer: int):
    try:
        nubmer = int(nubmer)
    except:
        return nubmer
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
        case 6:
            return '6️⃣'
        case 7:
            return '7️⃣'
        case 8:
            return '8️⃣'
        case 9:
            return '9️⃣'
        case 0:
            return '0️⃣'
        
        case _:
            return nubmer

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
        
async def use_for(message: types.Message, list_schedule, id_user, method): 
    numbers_couple = 0
    line = ''
    time = {1: '8:30-10:00', 2: '10:10-11:40', 3: '12:10-13:40', 4: '13:50-15:20', 5: '15:30-17:00'}
    for day in list_schedule:
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
        case 'notification':
            return [list_schedule, line]
        case 'text':
            return line


async def display_the_schedule(id_user, message: types.Message, day, method):
    try:
        cache_group_users = CacheGroupUsers()
        id_group = cache_group_users.cache_group_users_dict[id_user]
        end_list = await check(id_group, day)
        match method:
            case 'text':
                return await use_for(message, end_list.copy(), id_user, method)
            case 'notification':
                return await use_for(message, end_list.copy(), id_user, method)            
            case _:
                await use_for(message, end_list.copy(), id_user, method)
        # return await use_for(message, end_list.copy(), id_user, method)
    except (AttributeError, KeyError):
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
    builder.add(types.KeyboardButton(text="Экзамены"))
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
    current_day = CurrentDay()
    info_class = await display_the_schedule(
        message.from_user.id, message,  
        await check_week(await current_day.today_day_week()), 'text'
    )
    if await current_day.today_day_week() == 6:
        info_week = await week()
        await message.answer(f'{info_week}\n\nВ воскресенье пар нет!')
        return
    if info_class is None:
        await message.answer('❌ Выберите пожалуйста группу при помощи команды /group')    
    else:
        info_week = await week()
        await message.answer(f'{info_week}\n\n{info_class}', parse_mode="HTML")
        
@router.message(Command('while_time'))
async def time_while(message: types.Message):
    if message.from_user.id == 1752086646:
        await while_time()

@router.message(F.text == 'Завтрашние пары')
async def tomorrow_class(message: types.Message):
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
    if await current_day.today_day_week() == 5:
        info_week = await week()
        await message.answer(f'{info_week}\n\nВ воскресенье пар нет!')
        return
    if info_class is None:
        await message.answer('❌ Выберите пожалуйста группу при помощи команды /group')
        
    else:
        info_week = await week()
        await message.answer(f'{info_week}\n\n{info_class}', parse_mode='HTML')

    
@router.message(F.text == "Экзамены")
async def return_exams(message: types.Message):
    cache_group_users = CacheGroupUsers()
    id_group = cache_group_users.cache_group_users_dict[message.from_user.id]   
    if id_group is None:
        await message.answer("❌ Выберите пожалуйста группу при помощи команды /group")
        return 
    data_exams = await check(
        id_group, "exams"
    )
    if not data_exams:
        await message.answer("Расписание экзаменов не выставлено")
        return 
    answer = ""
    
    for i in range(len(data_exams)):
        exam = f"exam_{i+1}"
        date = data_exams[exam]["date"]
        name = data_exams[exam]["name"]
        auditorium_number = data_exams[exam]["auditorium_number"]
        audit_number_emoji = list(map(emoji_number_couple, auditorium_number))
        auditorium_number_emoji = f"{audit_number_emoji[0]}{audit_number_emoji[1]}{audit_number_emoji[2]}"
        type_ = data_exams[exam]["type"]
        date_answer = f"🗓 Дата и время:  <u><i>{date}</i></u>"
        name_answer = f"Предмет: {name}"
        auditorium_number_answer = f"Номер аудитории : {auditorium_number_emoji}"
        # auditorium_number_answer = f"Номер аудитории : 3️⃣4️⃣5️⃣"
        type_answer = f"Консультация или Экзамен: <u><i>{type_}</i></u>"
        answer+=f"{date_answer}\n{name_answer}\n{auditorium_number_answer}\n{type_answer}\n\n"

    await message.answer(answer, parse_mode="HTML")
    