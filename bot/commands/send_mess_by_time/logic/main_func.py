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
from cache_group_users.cache_group_user import CacheGroupUsers
from lessons.current_day import CurrentDay
from lessons.score_week import week
from asyncio import CancelledError



async def keyboard_callback_edit():
    builder = InlineKeyboardBuilder()
    await CallbackButton('Удалить уведомление', 'edit', builder)()
    return builder.as_markup()

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
        print(time_to_slep)
        await asyncio.sleep(time_to_slep)
        current_day = CurrentDay()
        day = await current_day.today_day_week()
        current_day = CurrentDay()
        if await current_day.today_day_week() == 6:
            info_week = await week()
            await message.reply(f'{info_week}\n\nВ воскресенье пар нет!')
        else:
            await display_the_schedule(
                user_id,
                message, 
                await check_week(
                    day
                ),
                'answer'
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
        await asyncio.sleep(time_to_slep)
        current_day = CurrentDay()
        day = await current_day.today_day_week()
        await display_the_schedule(
            id_user,
            message, 
            await check_week(
                day
            ),
            'bot_send'
        )   
        await asyncio.sleep(10) 
        time_to_slep = await count_next_notification.count()
        print(time_to_slep)
        await asyncio.sleep(time_to_slep)

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
            await display_the_schedule(
                id_user,
                message, 
                await check_week(
                    day
                ),
                'answer'
            )   
        await asyncio.sleep(6) 
        time_to_slep = await count_next_notification.count()
        print(time_to_slep)
        await asyncio.sleep(time_to_slep-6)

