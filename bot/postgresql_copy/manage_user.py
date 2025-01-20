from sqlalchemy.exc import IntegrityError
from sqlalchemy import Select
from .tables import Users, engine
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
from time import sleep


class ManageUser:
    def __init__(
            self, id_user: int,
            user_name: str, id_group: str
        ):
        self.id_user = id_user
        self.user_name = user_name
        self.id_group = id_group

    async def create_user(self):
        async with AsyncSession(autoflush=False, bind=engine) as session:
            async with session.begin(): # Для транзакций
                user = Users(
                    id_user=self.id_user,
                    user_name=self.user_name,
                    id_group=f"schedule_{self.id_group}"
                )
                try:
                    session.add(user)
                    await session.commit()
                except:
                    print(user)
                    return user
                 # именна вот эта команда не будет давать блокировать запросы
            # не забыть добавить отправление сообщений в логи

    async def update_group_at_user(self, new_id_group: str):
        async with AsyncSession(autoflush=False, bind=engine) as session:
            async with session.begin():
                user = await session.execute(Select(Users).filter(Users.id_user==self.id_user).limit(1))
                user = user.scalar_one_or_none()
                if user:
                    user.id_group = f"schedule_{new_id_group}"
                    user.user_name = self.user_name
                    await session.commit()
                else:
                    print(user)
                    pass
                    # отправка логов в бота об ошибке
                    # отправка пользователю, что не удалось выбрать группу



# async def main():
#     test = ManageUser(111111, None, '1008')
#     t = await test.create_user()
#     if t:
#         print("Такой пользователь уже есть")
#         sleep(5)
#         await test.update_group_at_user("1005")

# asyncio.run(main())