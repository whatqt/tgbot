from aiogram.filters import CommandObject
from aiogram import types
from postgresql.management.manage_send_mess.manage_mess_by_time import \
    ManageSendMessTime
from postgresql.management.manage_send_mess.time_set import ManageTime
from commands.select_group.callback import CallbackButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from commands.send_mess_by_time.text import text_info
from .logic_calculation_time import CountNextNotification
import asyncio
from lessons.week.week import display_the_schedule
from lessons.score_week import check_week
from lessons.current_day import CurrentDay
from sqlalchemy.exc import IntegrityError



async def keyboard_callback_edit():
    builder = InlineKeyboardBuilder()
    await CallbackButton('Удалить уведомление', 'edit', builder)()
    return builder.as_markup()

async def send_mess_by_time(
    message: types.Message,
    command: CommandObject,
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

    try:
        await manage_send_mess_time.insert_time(
            time_from_db
        )

    except IntegrityError:
        time_db = await manage_send_mess_time.return_time_by_id()
        await message.reply(
            text_info["there_time"].format(time_db),
            reply_markup=await keyboard_callback_edit()
        )
        return

    count_next_notification = CountNextNotification(manage_time.time)
    await message.reply(
        f"Уведомление установлено на {command.args}",
        reply_markup=await keyboard_callback_edit()
    )

    while True:
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
        await asyncio.sleep(10) 
        time_to_slep = await count_next_notification.count()
        print(time_to_slep)
        await asyncio.sleep(time_to_slep)