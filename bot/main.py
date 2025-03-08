import asyncio
from aiogram import Bot, Dispatcher
from commands.select_group import group
from commands import feeadback_and_report, start, \
    schedule, help, admin, send_info_update, send_logs
from commands.send_logs import CustomErrorHandler
from commands.cache_update import cache_update
from lessons.week import week
import os
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from cache_group_users import launch
from commands.send_mess_by_time import send_mess_by_time
import logging






load_dotenv()
async def main():
    bot = Bot(token=os.getenv('TOKEN_BOT'))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers( 
        cache_update.router, feeadback_and_report.router, 
        group.router, start.router, 
        week.router, schedule.router,
        help.router, admin.router,
        send_info_update.router, send_mess_by_time.router,
        launch.router, send_logs.router,
    )
    error_handler = CustomErrorHandler()
    logging.basicConfig(level=logging.INFO, filename="logs.log",filemode="w")
    logging.getLogger().addHandler(error_handler)

    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot)

print('Бот запущен')
asyncio.run(main())

# сделать логирование
# сделать так, чтобы при ошибке было уведомление об этом
# разобраться с багом 19:59
# настроить общий репозиторий
