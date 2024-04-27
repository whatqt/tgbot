from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram import types
import asyncio
from aiogram import Bot
from parser.parser import *
from func_cache.cache import generator_id, generator_schedule
from func_cache.lessen import *
import threading




router = Router()
bot = Bot('6573990032:AAGRALx8BGzMNIj1KulH8A_onrv6mKLENEw')


async def change_id(group_id):
   await group(URL, group_id, tables)
   await asyncio.sleep(0.1)

async def upgrade_cache(id_group):
    print('Кэш обновляется')
    lst = []
    lst_two = []
    mygenerator = generator()
    day = 1
    while day <= 6:
        await html_result_group_one(tables['first_week_1'], tables['first_week_2'], day, lst)
        day += 1
        record_cache(id_group, (next(mygenerator)), lst.copy())
        lst.clear()

    day_two = 1
    while day_two <= 6:
        await html_result_group_two(tables['second_week_1'], tables['second_week_2'], day_two, lst_two)
        day_two += 1
        record_cache(id_group, (next(mygenerator)), lst_two.copy())
        lst_two.clear()

    await asyncio.sleep(0.1)
    print('Кэш обновился')


@router.message(Command('cache'))
async def upgrade_ch_by_time(message: types.Message):
    if message.from_user.id == 1752086646:
        result = await group_check()
        new_result = result.split()
        while True:
            error = []            
            schedule_generation =  generator_schedule()
            id_generation =  generator_id()
            a = 1   
            while a <=32:
                try:
                    if new_result[3] != '200':
                        await bot.send_message(-4149670794, f'#кэш\nОбновление кэша не началось, так как сайт недоступен\nПодробности о http статусе:\n{result}')
                        print('Обновление кэша не началось')
                        return                    
                    
                    print(f'Группа по словарю: {a}')
                    await change_id(next(id_generation))
                    await upgrade_cache(next(schedule_generation))
                    a+=1
                    await asyncio.sleep(0.1)
                except IndexError as i: #error groups 5, 22, 23, 24, 29, 31, 32, 33
                    print(i)
                    error.append(a)                    
                    a+=1
                    continue
                except AttributeError as s:
                    print(s)
                    error.append(a)                    
                    a+=1
                    continue
            await bot.send_message(-4149670794, f'#кэш\nКэш обновился\nГруппы которые не обновились: {error}')
            await asyncio.sleep(600)


