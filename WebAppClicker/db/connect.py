import asyncpg
import asyncpg.cursor 


async def create_connection():
    connection = await asyncpg.connect(
        host="127.0.0.1", 
        port="5432",
        user="postgres",
        password="A123B567E",
        database="clicker"
        )
    return connection
