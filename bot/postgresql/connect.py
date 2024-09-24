import asyncpg 

# dsn = "dbname=tg_bot user=postgres password=A123B567E host=127.0.0.1"

async def create_connection():
    connection = await asyncpg.connect(dsn='postgresql://postgres:A123B567E@127.0.0.1/tg_bot') #create_pool
    return connection


