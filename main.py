import asyncio
from aiogram import Bot, Dispatcher
from commands import cache_update, feeadback_and_report, group, start, schedule, help, admin
from send_mess_by_time import check_time_for_mess
from handlears import week
import os



async def main():
    bot = Bot(token=os.getenv('TOKEN_BOT'))
    dp = Dispatcher()
    dp.include_routers( 
        cache_update.router, feeadback_and_report.router, 
        group.router, start.router, 
        week.router, schedule.router,
        help.router, admin.router,  
        check_time_for_mess.router
        )
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot)


print('Бот запущен')
asyncio.run(main())

