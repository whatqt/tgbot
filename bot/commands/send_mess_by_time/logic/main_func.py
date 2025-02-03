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




async def keyboard_callback_edit():
    builder = InlineKeyboardBuilder()
    await CallbackButton('Удалить уведомление', 'edit', builder)()
    return builder.as_markup()

async def send_mess_by_time(
    message: types.Message,
    command: CommandObject,
    ):
    cache_group_users = CacheGroupUsers()
    user_id = message.from_user.id
    if command.args is None:
        await message.reply(
            text_info["none_args"]
        )
        return
    if user_id not in cache_group_users.cache_group_users_dict:
        await message.reply(
            text_info["id_group_none"]
        )
        return

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
        await display_the_schedule(
            user_id,
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
