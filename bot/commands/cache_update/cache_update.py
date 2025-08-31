import sys
sys.path.append('...')
from aiogram import Router
from aiogram.filters import Command
from aiogram import types
import asyncio
from aiogram import Bot
from parser.parser_schedule import *
from parser.parser_exams import GetExams
from .tools.cache import generator_id
from .tools.lessen import * # generator_schedule - от сюда
from .tools.all_course import all_course
import os
from dotenv import load_dotenv
from logic_logs.file.logger import logger


load_dotenv()


router = Router()
bot = Bot(token=os.getenv('TOKEN_BOT'))

async def change_id(group_id):
    manage_parser = ManageParser()
    result = await manage_parser.get_html_schedule(
        group_id, tables
    )

    return result
   
async def upgrade_cache_schedule(schedule: str):
    logger.debug(f'Кэш группы {schedule} обновляется')
    manage_parser = ManageParser()
    lst = []
    lst_two = []
    weekday = generator_weekday()
    day = 1
    day_two = 1
    while day <= 6:
        await manage_parser.html_result_group_week(
            'first_week_1', 'first_week_2',
            day, lst
        )
        day += 1
        await record_cache_schedule(schedule, (next(weekday)), lst.copy())
        lst.clear()

    while day_two <= 6:
        await manage_parser.html_result_group_week(
           'second_week_1', 'second_week_2', 
           day_two, lst_two
        )
        day_two += 1
        await record_cache_schedule(schedule, (next(weekday)), lst_two.copy())
        lst_two.clear()

    await asyncio.sleep(0.1)
    logger.debug(f'Кэш группы {schedule} обновился')

async def upgrade_cache_exams(schedule_id: str):
    id_group: int = schedule_id.split("_")[1]
    get_exams = GetExams()
    exams = await get_exams.get_text_and_return_exams(id_group)
    await record_cache_exams(schedule_id, exams)


@router.message(Command('cache'))
async def upgrade_ch_by_time(message: types.Message):
    if message.from_user.id == 1752086646:
        while True:
            error = {}           
            schedule_generation = generator_schedule()
            id_generation =  generator_id()
            group = 1   
            while group <=43:
                try:
                    id_group = next(id_generation)
                    schedule = next(schedule_generation)
                    result = await change_id(id_group)
                    if result is False:
                        await bot.send_message(
                            -4112086004, 
                            f"@what_whatqwe\nCайт не доступен. Повторный парсинг будет через 10 минут"
                        )
                        logger.warning('Сайт не доступен. Повторный парсинг будет через 10 минут')
                        await asyncio.sleep(600)
                        continue
                    await upgrade_cache_schedule(schedule)
                    await upgrade_cache_exams(schedule)
                    group+=1
                    await asyncio.sleep(0)
                except Exception as e:
                    logger.warning(f"Ошибка при обновление кэша:{e}")
                    name_group = all_course[id_group].split(' ')[3]
                    if not error:
                        error[str(e)] = [name_group]
                    else:
                        list_id: list = error.get(str(e))
                        list_id.append(name_group)
                    group+=1
                    continue
            if error:
                msg = f'@what_whatqwe\nКэш обновился\nГруппы которые не обновились: {error}'
            else: msg = f'Кэш обновился'
            await bot.send_message(
                -4112086004, 
                msg
            )
            logger.debug("Кэш обновлён")
            await asyncio.sleep(600)


