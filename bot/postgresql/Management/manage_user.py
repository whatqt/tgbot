from sqlalchemy.exc import IntegrityError
from sqlalchemy import Select
from postgresql.tables import Users, engine
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
from time import sleep
from logic_logs.log_manage_user import LogManageUser



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
                    log_manager_user = LogManageUser(
                        self.id_user, 
                        self.user_name,
                        self.id_group
                    )                    
                    await log_manager_user.send_about_create_user()
                    
                except IntegrityError:
                    return user


    async def update_group_at_user(self, new_id_group: str):
        async with AsyncSession(autoflush=False, bind=engine) as session:
            async with session.begin():
                user = await session.execute(
                    Select(Users).filter(
                        Users.id_user==self.id_user
                    ).limit(1)
                )
                user = user.scalar_one_or_none()
                if user:
                    user.id_group = f"schedule_{new_id_group}"
                    user.user_name = self.user_name
                    await session.commit()
                    log_manager_user = LogManageUser(
                        self.id_user, 
                        self.user_name,
                        self.id_group
                    )                    
                    await log_manager_user.send_about_update_user()
                else:
                    print(user)
                    pass

    async def get_all_id_users(self):
        async with AsyncSession(autoflush=False, bind=engine) as session:
            async with session.begin():
                users = await session.execute(Select(Users.id_user))
                return users.all()
    