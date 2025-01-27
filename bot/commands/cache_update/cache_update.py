import sys
sys.path.append('...')
from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
import asyncio
from aiogram import Bot
from parser.parser_schedule import *
# from parser.parser_exams import *
# from .tools.cache import generator_id, generator_schedule
from .tools.cache import generator_id
from .tools.lessen import * # generator_schedule - от сюда
import os
from dotenv import load_dotenv



load_dotenv()


router = Router()
bot = Bot(token=os.getenv('TOKEN_BOT'))

async def change_id(group_id):
   manage_parser = ManageParser()

   await manage_parser.get_html_schedule(
       group_id, tables
    )

async def upgrade_cache(schedule):
    print('Кэш обновляется')
    manage_parser = ManageParser()
    lst = []
    lst_two = []
    weekday = generator_weekday()
    day = 1
    day_two = 1
    while day <= 6:
        # await manage_parser.html_result_group_week(tables['first_week_1'], tables['first_week_2'], day, lst)
        await manage_parser.html_result_group_week(
            'first_week_1', 'first_week_2',
            day, lst
        )
        day += 1
        await record_cache(schedule, (next(weekday)), lst.copy())
        lst.clear()

    while day_two <= 6:
        await manage_parser.html_result_group_week(
           'second_week_1', 'second_week_2', 
           day_two, lst_two
        )
        day_two += 1
        await record_cache(schedule, (next(weekday)), lst_two.copy())
        lst_two.clear()
    #data_exams = await get_exams(id_group)

    await asyncio.sleep(0.1)
    print('Кэш обновился')


@router.message(Command('cache'))
async def upgrade_ch_by_time(message: types.Message):
    if message.from_user.id == 1752086646:
        while True:
            error = {}           
            schedule_generation = generator_schedule()
            id_generation =  generator_id()
            group = 1   
            while group <=32:
                try:
                    print(f'Группа по словарю: {group}')
                    id_group = next(id_generation)
                    schedule = next(schedule_generation)
                    await change_id(id_group)
                    await upgrade_cache(schedule)
                    #data_exams = await get_exams(id_group)
                    #await get_data_exams(data_exams, schedule)
                    group+=1
                    await asyncio.sleep(0)
                except IndexError as i:
                    print(i)
                    error[i] = schedule_generation            
                    group+=1
                    continue
                except AttributeError as a: 
                    print(a)
                    error[a] = schedule_generation            
                    group+=1
                    continue
            await bot.send_message(
                -4112086004, 
                f'#кэш\nКэш обновился\nГруппы которые не обновились: {error}'
            )

            await asyncio.sleep(600)


