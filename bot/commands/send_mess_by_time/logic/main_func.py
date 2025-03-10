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
from mongodb.send_mess_time.cache_send_mess_time import CacheSendMessTime
from math import ceil
from lessons.current_day import CurrentDay
from lessons.score_week import week
from aiogram import Bot
import os


bot = Bot(token=os.getenv("TOKEN_BOT"))

async def keyboard_callback_edit():
    builder = InlineKeyboardBuilder()
    await CallbackButton('Удалить уведомление', 'edit', builder)()
    return builder.as_markup()

async def chek_schedule_for_pairs(unprocessed_schedule: list) -> bool:
    for _class in unprocessed_schedule:
        if _class == "":
            continue
        else:
            return True
    return False



async def send_mess_by_time(
    message: types.Message,
    command: CommandObject,
    ):
    user_id = message.from_user.id
    manage_time = ManageTime(command.args)
    time_from_db = await manage_time.date()
    manage_send_mess_time = ManageSendMessTime(
        user_id
    )
    cache_send_mess_time = CacheSendMessTime(user_id)

    try:
        await manage_send_mess_time.insert_time(
            time_from_db
        )
        full_time = time_from_db.time()

        await cache_send_mess_time.insert_user(
            f"{full_time.hour}:{full_time.minute}"
        )

    except IntegrityError:
        # оповещение, что уже есть уведомление
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
        print(ceil((time_to_slep-0.4)))
        await asyncio.sleep(ceil(time_to_slep)-0.4)
        current_day = CurrentDay()
        day = await current_day.today_day_week()
        if await current_day.today_day_week() == 6:
            await asyncio.sleep(0.4)
            continue
        else:
            info_schedule = await display_the_schedule(
                user_id,
                message, 
                await check_week(
                    day
                ),
                'notification',
            )   
            unprocessed_schedule, processed_schedule = info_schedule
            result = await chek_schedule_for_pairs(unprocessed_schedule)
            if result is False:
                await asyncio.sleep(0.4)
                continue
            else:            
                info_week = await week()
                await message.answer(
                    f"{info_week}\n{processed_schedule}",
                    parse_mode="HTML"
                )
            
        await asyncio.sleep(6) 
        time_to_slep = await count_next_notification.count()
        print(time_to_slep)
        await asyncio.sleep(time_to_slep-6)

async def update_task(
    message: types.Message,
    id_user: int,
    ):
    cache_send_mess_time = CacheSendMessTime(id_user)
    info_at_notification = await cache_send_mess_time.find_user()
    count_next_notification = CountNextNotification(
        info_at_notification["time"]
    )
    manage_send_mess_time = ManageSendMessTime(
        id_user
    )
    manage_time = ManageTime(info_at_notification["time"])

    await manage_send_mess_time.insert_time(
        await manage_time.date()
    )

    while True:
        time_to_slep = await count_next_notification.count()
        print(time_to_slep)
        await asyncio.sleep(ceil(time_to_slep)-0.4)
        current_day = CurrentDay()
        day = await current_day.today_day_week()
        if await current_day.today_day_week() == 6:
            await asyncio.sleep(0.4)
            continue
        info_schedule = await display_the_schedule(
                id_user,
                message, 
                await check_week(
                    day
                ),
                'notification',
            )   
        unprocessed_schedule, processed_schedule = info_schedule
        result = await chek_schedule_for_pairs(unprocessed_schedule)
        if result is False:
            await asyncio.sleep(0.4)
            continue
        else:            
            info_week = await week()
            await bot.send_message(
                id_user,
                f"{info_week}\n\n{processed_schedule}",
                parse_mode="HTML"
            )
        await asyncio.sleep(6) 
        time_to_slep = await count_next_notification.count()
        print(time_to_slep)
        await asyncio.sleep(time_to_slep-6)

async def admin_send_class_by_time(
    message: types.Message,
    command: CommandObject
    ):

    id_user = int(command.args)
    if id_user:
        cache_send_mess_time = CacheSendMessTime(id_user)

        manage_time = ManageTime("23:20")
        time_from_db = await manage_time.date()
        manage_send_mess_time = ManageSendMessTime(
            id_user
        )
        print(f"ВРЕМЯ С БД {time_from_db}")
        try:
            await manage_send_mess_time.insert_time(time_from_db)
            cache_send_mess_time = CacheSendMessTime(id_user)
            await cache_send_mess_time.insert_user("23:20")
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
        current_day = CurrentDay()
        if await current_day.today_day_week() == 6:
            info_week = await week()
            await message.reply(f'{info_week}\n\nВ воскресенье пар нет!')
        else:
            info_schedule = await display_the_schedule(
                id_user,
                message, 
                await check_week(
                    day
                ),
                'notification',
            )   
            unprocessed_schedule, processed_schedule = info_schedule
            result = await chek_schedule_for_pairs(unprocessed_schedule)
            if result is False:
                await asyncio.sleep(1) 
                continue
            else:            
                info_week = await week()
                await bot.send_message(
                    id_user,
                    f"{info_week}\n\n{processed_schedule}",
                    parse_mode="HTML"
                )

             
        await asyncio.sleep(6) 
        time_to_slep = await count_next_notification.count()
        print(time_to_slep)
        await asyncio.sleep(time_to_slep-6)

