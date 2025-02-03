from sqlalchemy.exc import IntegrityError
from sqlalchemy import Select
from postgresql.tables import engine, SendMessTime
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
from time import sleep
from logic_logs.log_manage_user import LogManageUser




class ManageSendMessTime:
    def __init__(self, id_user):
        self.id_user = id_user
        # разобраться, как перекинуть суда сессию

    async def insert_time(self, time):
        async with AsyncSession(autoflush=False, bind=engine) as session:
            async with session.begin():
                # await insert_time 
                # manage_time = ManageTime(time)
                create_time = SendMessTime(
                    id_user=self.id_user,
                    time_set=time
                )
                session.add(create_time)
                await session.commit()
            
    async def delete_time(self):
        async with AsyncSession(autoflush=False, bind=engine) as session:
            async with session.begin():
                obj = await session.execute(
                    Select(SendMessTime).filter(
                        SendMessTime.id_user==self.id_user
                    )
                )
                obj = obj.scalar_one()
                print(obj)
                await session.delete(obj)
                await session.commit() 

    async def return_all_user(self):
        async with AsyncSession(autoflush=False, bind=engine) as session:
            async with session.begin():
                obj = await session.execute(
                    Select(SendMessTime)
                )
                obj = obj.all()
                session.expunge_all()
                return obj[0]
    
    async def return_time_by_id(self):
        async with AsyncSession(autoflush=False, bind=engine) as session:
            async with session.begin():
                obj = await session.execute(
                    Select(SendMessTime).filter(
                        SendMessTime.id_user==self.id_user
                    )
                )
                time = obj.scalar_one()
                result_time = str(time.time_set).split(' ', 1)[1]
                return result_time



    
    




