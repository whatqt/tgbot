from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
import asyncio
from aiogram import Bot
from parser.parser_schedule import *
from parser.parser_exams import *
from .tools.cache import generator_id, generator_schedule
from .tools.lessen import *
import os
from dotenv import load_dotenv



load_dotenv()


router = Router()
bot = Bot(token=os.getenv('TOKEN_BOT'))

async def change_id(group_id):
   await group(URL, group_id, tables)

async def upgrade_cache(id_group):
    print('Кэш обновляется')
    lst = []
    lst_two = []
    weekday = generator_weekday()
    day = 1
    while day <= 6:
        await html_result_group_one(tables['first_week_1'], tables['first_week_2'], day, lst)
        day += 1
        await record_cache(id_group, (next(weekday)), lst.copy())
        lst.clear()

    day_two = 1
    while day_two <= 6:
        await html_result_group_two(tables['second_week_1'], tables['second_week_2'], day_two, lst_two)
        # добавить суда mongodb
        day_two += 1
        await record_cache(id_group, (next(weekday)), lst_two.copy())
        lst_two.clear()
    data_exams = await get_exams(id_group)

    await asyncio.sleep(0)
    print('Кэш обновился')


@router.message(Command('cache'))
async def upgrade_ch_by_time(message: types.Message):
    if message.from_user.id == 1752086646:
        while True:
            status_code = await group_check()
            error = []            
            schedule_generation =  generator_schedule()
            id_generation =  generator_id()
            group = 1
            if status_code != 200:
                await bot.send_message(
                -4112086004, 
                f'#кэш\nОбновление кэша не началось, так как сайт недоступен\nHTTP код - {status_code}\nПовторная попытка будет через 5 минут'
                )

                print('Обновление кэша не началось')
                await asyncio.sleep(300)
                continue        
            while group <=32:
                try:
                    if status_code != 200:
                        await bot.send_message(
                            -4112086004, 
                            f'#кэш\nОбновление кэша не началось, так как сайт недоступен\nHTTP код - {status_code}')
                        print('Обновление кэша не началось')
                        break
                    print(f'Группа по словарю: {group}')
                    id_group = next(id_generation)
                    schedule = next(schedule_generation)
                    await change_id(id_group)
                    await upgrade_cache(schedule)
                    data_exams = await get_exams(id_group)
                    await get_data_exams(data_exams, schedule)
                    group+=1
                    await asyncio.sleep(0.1)
                except IndexError as i: #error groups 5, 22, 23, 24, 29, 31, 32, 33
                    print(i)
                    error.append(group)                    
                    group+=1
                    continue
                except AttributeError as s: 
                    print(s)
                    error.append(group)                    
                    group+=1
                    continue
            await bot.send_message(-4112086004, f'#кэш\nКэш обновился\nГруппы которые не обновились: {error}')
            await asyncio.sleep(600)


