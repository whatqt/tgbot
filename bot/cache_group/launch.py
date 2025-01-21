from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram import types
from dotenv import load_dotenv
import os
from cache_group.cache_group_user import CacheGroupUsers, cache_group_users_dict



load_dotenv()

router = Router()
bot = Bot(token=os.getenv('TOKEN_BOT'))

@router.message(Command('cache_group_user'))
async def lauch_cache_group_user(message: types.Message):
    cache_group_users = CacheGroupUsers(cache_group_users_dict)
    await cache_group_users.record_all_user()
    await message.answer("Кэш пользователей обновлён!")