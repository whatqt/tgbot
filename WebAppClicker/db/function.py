from .connect import create_connection
import asyncpg



async def get_clicks(id_user):
    try:
        cursor = await create_connection()
        sql_get_clicks = f"""
        SELECT clicks_score FROM data_user
        WHERE id_user = {id_user}
        """
        data = await cursor.fetchrow(sql_get_clicks)
        return data[0]
    finally: await cursor.close()

async def update_clicks(id_user, clicks):
    try:
        cursor = await create_connection()
        sql_update_clicks = f"""
        UPDATE data_user
        SET clicks_score = {clicks}
        WHERE id_user = {id_user}
        """
        await cursor.execute(sql_update_clicks)
    finally: await cursor.close()