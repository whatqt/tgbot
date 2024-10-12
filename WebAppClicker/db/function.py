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

async def insert_data_of_active_raid(
        id_user,
        reward_in_gold, reward_in_token,
        time_end_raid
    ):

    try:
        cursor = await create_connection()
        sql_data = f"""
            INSERT INTO data_of_active_raid VALUES 
            (
                {id_user}, {reward_in_gold},
                {reward_in_token}, {time_end_raid}   
            );
        """
        await cursor.execute(sql_data)
    finally: await cursor.close()
     
async def update_golds_tokens(id_user, golds, tokens):
    try:
        cursor = await create_connection()
        sql_update = f"""
            UPDATE data_users
            SET quantity_gold = quantity_gold + {golds},
                quantity_token = quantity_token + {tokens}
            WHERE id_user = {id_user};
        """
        await cursor.execute(sql_update)
        print("Данные обновились")
    finally: await cursor.close()


async def delete_data_of_active_raid(id_user):
    try:
        cursor = await create_connection()
        sql_data = f"""
            DELETE FROM data_of_active_raid
            WHERE id_user = {id_user}
        """
        await cursor.execute(sql_data)
        print("Данные удалились")
    finally: await cursor.close()
