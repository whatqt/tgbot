from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram import types
from aiogram import Bot
import os
from postgresql.management.manage_send_mess.manage_mess_by_time import \
    ManageSendMessTime
from postgresql.management.manage_send_mess.time_set import ManageTime
from commands.select_group.callback import CallbackButton
from postgresql.management.manage_user import ManageUser
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv
from .text import text_info
from datetime import datetime, timedelta
from .logic_calculation_time import CountNextNotification
import asyncio
from lessons.week.week import display_the_schedule
from lessons.score_week import check_week
from lessons.current_day import CurrentDay




load_dotenv()
router = Router()
users_use_notification = []


bot = Bot(token=os.getenv('TOKEN_BOT'))


@router.message(Command("send_class_by_time"))
async def send_mess_by_time(
    message: types.Message,
    command: CommandObject
    ):
    if command.args is None:
        await message.reply(
            text_info["none_args"]
        )
        return
    
    manage_time = ManageTime(command.args)
    time_from_db = await manage_time.date()

    manage_send_mess_time = ManageSendMessTime(
        message.from_user.id
    )
    await manage_send_mess_time.insert_time(
        time_from_db
    )
    count_next_notification = CountNextNotification(manage_time.time)
    users_use_notification.append(message.from_user.id)

    while True:
        if message.from_user.id in users_use_notification:
            time_to_slep = await count_next_notification.count()
            print(time_to_slep)
            await asyncio.sleep(time_to_slep)
            current_day = CurrentDay()
            day = await current_day.today_day_week()
            await display_the_schedule(
                message.from_user.id, 
                message, 
                await check_week(
                    day
                ),
                'answer'
            )   
            
            time_to_slep = await count_next_notification.count()
            print(time_to_slep)
            await asyncio.sleep(time_to_slep)

        else:
            await manage_send_mess_time.delete_time()
            await message.answer("Отправка уведомлений была остановлена")




