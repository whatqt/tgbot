import asyncpg 
from postgresql.connect import create_connection
from aiogram import Bot
from datetime import datetime



bot = Bot(token="6707038280:AAGFfo73_3sf_Es0ptpA5uzPzrcDnOMAjRc")

async def insert_into_table(id_user, user_name, id_group):
    cursor = await create_connection()
    try:
        insert_info = f'''
        INSERT INTO users VALUES ('{id_user}', '{user_name}', 'schedule_{id_group}')
        '''
        await cursor.execute(insert_info)
        print(f'Имя пользователя: {user_name}\nid пользователя: {id_user}\nгруппа пользователя: {id_group}')
        print('Пользователь добавлен в базу данных 📝')
        await bot.send_message(
        -1001948152320, 
        f'#база_данных\nИмя пользователя: {user_name}\nid пользователя: {id_user}\nгруппа пользователя: {id_group}'
        )
    except asyncpg.exceptions.UniqueViolationError:
        print('Пользователь уже есть в базе данных 📋 ') 
        print(f'id пользователя {id_user} | user_name пользователя {user_name}')
        update_user_group = f'''
        UPDATE users
        SET id_group = 'schedule_{id_group}'
        WHERE id_user = {id_user}
        ''' 
        await cursor.execute(update_user_group)
        print('id группы пользователя был успешно обновлён ✅')
        print('\n')
        await bot.send_message(
        -1001948152320, 
        f'#база_данных\nПользователь уже есть в базе данных 📋\nid пользователя {id_user} | user_name пользователя {user_name}\nid группы пользователя был успешно обновлён ✅'
        )     
    finally:
        await cursor.close()


async def check_id_group(id_user):
    cursor = await create_connection()
    try:
        select_id_user = f'''
        SELECT id_user,
        CASE
            WHEN id_user = {id_user}
                THEN id_group
            ELSE 'No'
        END AS yes
        FROM users
        '''
        result = await cursor.fetch(select_id_user)
        for info in result:
            new_info = str(info)
            if new_info.split(' ')[1] == f'id_user={id_user}':
                return(new_info.split(' ')[2].split("'", 2)[1])
    finally:
        await cursor.close()                

async def insert_into_time(id_user, hour, minute):
    try:
        cursor = await create_connection()
        time_set = f'''
        INSERT INTO send_mess_time VALUES ('{id_user}', TIMESTAMP '{2024}-{4}-{18} {hour}:{minute}:{00}')
        '''
        await cursor.execute(time_set)
    finally:
        await cursor.close()    

async def select_time_str(id_user):
    try:
        cursor = await create_connection()
        select_from = f'''
        SELECT id_user,
        CASE
            WHEN id_user = {id_user}
                THEN time_set
            ELSE NULL
        END AS yes
        FROM send_mess_time
        '''
        result = await cursor.fetch(select_from)
        for info_time in result:
            new_info_time = str(info_time).split(' ', maxsplit=2)[2]
            if new_info_time != 'yes=None>':
                result = new_info_time.split('(')[1].split(')')[0].replace(', ', '', 2).split(', ', 1)[1].replace(', ', ':')
                # print(result)
                return result
    finally:
        await cursor.close()      

async def select_time_time_int(id_user):
    try:
        cursor = await create_connection()
        select_from = f'''
        SELECT id_user,
        CASE
            WHEN id_user = {id_user}
                THEN time_set
            ELSE NULL
        END AS yes
        FROM send_mess_time
        '''
        result_one = await cursor.fetch(select_from)
        for info_time in result_one:
            new_info_time = str(info_time).split(' ', maxsplit=2)[2]
            if new_info_time != 'yes=None>':
                result = new_info_time.split('(')[1].split(')')[0]
                result_str = result.replace(', ', '-', 2).replace(', ', ' ', 1).replace(', ', ':')
                # print(info_time)
                return datetime.strptime(result_str, '%Y-%m-%d %H:%M')
            
    finally:
        await cursor.close()   

async def delete_date_time(id_user):
    try:
        cursor = await create_connection()
        delete_date = f'''
        DELETE FROM send_mess_time
            WHERE id_user = {id_user}
        '''
        await cursor.execute(delete_date)
    finally:
        await cursor.close()      
 

