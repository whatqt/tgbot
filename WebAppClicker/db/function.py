from .connect import create_connection
import asyncpg
from asyncpg.exceptions import UniqueViolationError
import asyncio




async def create_user_info(id_user, username):
    try:
        cursor = await create_connection()
        await cursor.execute(f"""
            INSERT INTO data_users VALUES 
            ({id_user}, '{username}', 3, 3, 0, 0);
            INSERT INTO lvl_users VALUES
            ({id_user});
        """
        # мб исопльзовать транзакции
        )    
    except UniqueViolationError: pass
    finally: 
        await cursor.close()

async def get_info_data_users(id_user):
    try:
        cursor = await create_connection()
        sql_data = f"""
        SELECT * FROM data_users
        WHERE id_user = {id_user}
        """
        data = await cursor.fetchrow(sql_data)
        print(data)
        return data
    finally: await cursor.close()

async def get_info_lvl_users(id_user):
    try:
        cursor = await create_connection()
        sql_data = f"""
        SELECT * FROM lvl_users
        WHERE id_user = {id_user}
        """
        data = await cursor.fetchrow(sql_data)
        print(data)
        return data
    finally: await cursor.close()