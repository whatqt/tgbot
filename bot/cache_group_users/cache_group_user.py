from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Select
from postgresql.tables import Users, engine
from logic_logs.file.logger import logger



class CacheGroupUsers:
	cache_group_users_dict = {}

	@classmethod
	async def add_user(cls, id_user, id_group):
		cls.cache_group_users_dict[id_user] = id_group

		return {id_user: id_group}

	async def record_all_user(self):
		async with AsyncSession(autoflush=False, bind=engine) as session:
			async with session.begin():  # надо ли это использовать при получение данных
				users = await session.execute(Select(Users))
				users = users.all()
				for user in users:
					new_user = user[0]
					await self.add_user(
						new_user.id_user,
						new_user.id_group
					)
				logger.info("Кэш пользователей был обновлён")	

