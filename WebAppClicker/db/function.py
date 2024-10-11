from .connect import create_connection
import asyncpg
import asyncio



async def get_data(id_user):
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

