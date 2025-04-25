from sqlalchemy.exc import IntegrityError
from sqlalchemy import Select
from postgresql.tables import Users, engine
from sqlalchemy.ext.asyncio import AsyncSession
from time import sleep
from logic_logs.chat.log_manage_user import LogManageUser
from logic_logs.file.logger import logger



class ManageUser:
    def __init__(
            self, id_user: int, user_name: str, 
            id_group: str
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
                    logger.debug(f"Пользователь {self.id_user} создан")
                    log_manager_user = LogManageUser(
                        self.id_user, 
                        self.user_name,
                        self.id_group
                    )                    
                    await log_manager_user.send_about_create_user()
                    
                except IntegrityError:
                    logger.debug(f"Пользователь {self.id_user} уже создан")
                    return user
                
                except Exception as e:
                    logger.error(f"Возникла ошибка при создание пользователя: {e}")

    async def update_group_at_user(self, new_id_group: str):
        async with AsyncSession(autoflush=False, bind=engine) as session:
            async with session.begin():
                try:
                    user = await session.execute(
                        Select(Users).filter(
                            Users.id_user==self.id_user
                        ).limit(1)
                    )
                    user = user.scalar_one_or_none()
                    user.id_group = f"schedule_{new_id_group}"
                    user.user_name = self.user_name
                    await session.commit()
                    logger.debug(f"У пользователя {self.id_user} обновлена группа")

                    log_manager_user = LogManageUser(
                        self.id_user, 
                        self.user_name,
                        self.id_group
                    )                    
                    await log_manager_user.send_about_update_user()
                except Exception as e:
                    logger.error(f"Ошибка при обновление пользователя {self.id_user} {e}")
                    

    async def get_all_id_users(self):
        async with AsyncSession(autoflush=False, bind=engine) as session:
            async with session.begin():
                users = await session.execute(Select(Users.id_user, Users.user_name))
                return users.all()
    