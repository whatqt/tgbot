import asyncio
from aiogram import Bot, Dispatcher
from commands.select_group import group
from commands import feeadback_and_report, start, \
    schedule, help, admin, send_info_update
from commands.send_mess_by_time import check_time_for_mess
from commands.cache_update_copy import cache_update
from lesson import week
import os
from aiogram.fsm.storage.memory import MemoryStorage
from commands.clicker import start_cliker
from dotenv import load_dotenv
from bot.cache_group.cache_group_user import CacheGroupUsers, cache_group_users_dict
from bot.cache_group import launch
from postgresql_copy.manage_user import ManageUser




load_dotenv()
# BOT = Bot(token=os.getenv('TOKEN_BOT'))
async def main():
    bot = Bot(token=os.getenv('TOKEN_BOT'))
    dp = Dispatcher(storage=MemoryStorage())
    # обязательно написать отдельный класс, который за это отвечает
    # а именно: за загрузку данных в cache_group_user 
    # (тоже будет переписан в класс, для лучшего понятия)
    # print(cache_group_users_dict)
    # await ManageUser(None, None, None).get_all_users()
    dp.include_routers( 
        cache_update.router, feeadback_and_report.router, 
        group.router, start.router, 
        week.router, schedule.router,
        help.router, admin.router,
        send_info_update.router,  check_time_for_mess.router,
        start_cliker.router, launch.router

        )
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot)

print('Бот запущен')
asyncio.run(main())

