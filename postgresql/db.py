import asyncpg 
from postgresql.connect import create_connection
from aiogram import Bot


bot = Bot(token="6573990032:AAGRALx8BGzMNIj1KulH8A_onrv6mKLENEw")


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
        -4149670794, 
        f'#база_данных\nИмя пользователя: {user_name}\nid пользователя: {id_user}\nгруппа пользователя: {id_group}'
        )
    except asyncpg.exceptions.UniqueViolationError:
        print('Пользователь уже есть в базе данных 📋 ') 
        print(f'id пользователя {id_user} | user_name пользователя {user_name}')
        selecet_from = '''
        SELECT id_user FROM users
        ''' 
        # await pool.execute(selecet_from)
        result = await cursor.fetch(selecet_from)
        for key in result:
            new_info = str(key)
            print(new_info.split(' ')[1])
            if new_info.split(' ')[1] == f'id_user={id_user}>':
                update_user_group = f'''
                UPDATE users
                SET id_group = 'schedule_{id_group}'
                WHERE id_user = {id_user}
                ''' 
                await cursor.execute(update_user_group)
                print('id группы пользователя был успешно обновлён ✅')
                print('\n')
                await bot.send_message(
                -4149670794, 
                f'#база_данных\nПользователь уже есть в базе данных 📋\nid пользователя {id_user} | user_name пользователя {user_name}\nid группы пользователя был успешно обновлён ✅'
                )     
                break
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

async def select_time_time(id_user):
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
                result = new_info_time.split('(')[1].split(')')[0]
                return result.replace(', ', ':')
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



#сделать автоудаление после достижения опредленного времени
#сделать изменение в бд, если пользователь захотел переставить время (мб 1 task и 2 task будут иметь единное решение)
#доделать класс, который упростит код
# asyncio.run(insert_into_time(1151, '1009'))  
# asyncio.run(insert_into_time(1752086646, '1008'))
# asyncio.run(select_all_time(1752086646))
