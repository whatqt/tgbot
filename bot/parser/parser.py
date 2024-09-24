import aiohttp
from bs4 import BeautifulSoup



URL = 'https://www.rubinst.ru/schedule'
tables = {'first_week_1': '', 'first_week_2': '',  'second_week_1': '', 'second_week_2': '', 'table_first_schedule': '', 'table_second_schedule': ''}

async def group(url, id_group, tables):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, cookies={'Group': id_group}) as resp:
            print(resp.status)
            soup = BeautifulSoup(await resp.read(), 'lxml')
            tables['table_first_schedule'] = soup.find('table', class_="schedule-table")
            tables['table_second_schedule'] = soup.find('table', class_="schedule-table").find_next('table', class_="schedule-table")
            #Первая неделя
            tables['first_week_1'] = tables['table_first_schedule'].find_all('tr', class_="odd")
            tables['first_week_2'] = tables['table_first_schedule'].find_all('tr', class_="even")
            #Вторая неделя
            tables['second_week_1'] = tables['table_second_schedule'].find_all('tr', class_="odd")
            tables['second_week_2'] = tables['table_second_schedule'].find_all('tr', class_="even")
    
async def check_table(tables_one, tables_two):
    len_tablse_one = 0
    len_tablse_two = 0
    
    for i in tables_one:
        len_tablse_one+=1
    for j in tables_two:
        len_tablse_two+=1
        
    return len_tablse_one+len_tablse_two

async def html_transform(table, element_list, day, new_list):
    score = 0
    for i in table[element_list]:
        info = i.get_text('th') 
        new_info = info.replace('th', ' ')   
        if score == day:
            new_list.append(new_info)
            break

        score+=1

async def html_result_group_one(table:dict, table_two:dict, day:int, new_list:list):
    score = 1
    if await check_table(tables['first_week_1'], tables['first_week_2']) == 4:
        while score <= 4:
            match score:
                case 1:
                    await html_transform(table, 0, day, new_list)
                case 2:
                    await html_transform(table_two, 0, day, new_list)
                case 3:
                    await html_transform(table, 1, day, new_list)
                case 4:
                    await html_transform(table_two, 1, day, new_list)
            score+=1

    elif await check_table(tables['first_week_1'], tables['first_week_2']) == 3:
        while score <= 3:
            match score:
                case 1:
                    await html_transform(table, 0, day, new_list)
                case 2:
                    await html_transform(table_two, 0, day, new_list)
                case 3:
                    await html_transform(table, 1, day, new_list)
            score+=1

    elif await check_table(tables['first_week_1'], tables['first_week_2']) == 5:
        while score <= 5:
            match score:
                case 1:
                    await html_transform(table, 0, day, new_list)
                case 2:
                    await html_transform(table_two, 0, day, new_list)
                case 3:
                    await html_transform(table, 1, day, new_list)
                case 4:
                    await html_transform(table_two, 1, day, new_list)
                case 5:
                    await html_transform(table, 2, day, new_list)
            score+=1
    
#функция для второй недели
async def html_result_group_two(table:dict, table_two:dict, day:int, new_list:list):
    score = 1
    if await check_table(tables['second_week_1'], tables['second_week_2']) == 4:
        while score <= 4:
            match score:
                case 1:
                    await html_transform(table, 0, day, new_list)
                case 2:
                    await html_transform(table_two, 0, day, new_list)
                case 3:
                    await html_transform(table, 1, day, new_list)
                case 4:
                    await html_transform(table_two, 1, day, new_list)
            score+=1

    elif await check_table(tables['second_week_1'], tables['second_week_2']) == 3:
        while score <= 3:
            match score:
                case 1:
                    await html_transform(table, 0, day, new_list)
                case 2:
                    await html_transform(table_two, 0, day, new_list)
                case 3:
                    await html_transform(table, 1, day, new_list)
            score+=1

    elif await check_table(tables['second_week_1'], tables['second_week_2']) == 5:
        while score <= 5:
            match score:
                case 1:
                    await html_transform(table, 0, day, new_list)
                case 2:
                    await html_transform(table_two, 0, day, new_list)
                case 3:
                    await html_transform(table, 1, day, new_list)
                case 4:
                    await html_transform(table_two, 1, day, new_list)
                case 5:
                    await html_transform(table, 2, day, new_list)
            score+=1

async def group_check():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=URL) as resp:
            print(resp.status)
            match resp.status:
                case 200:
                    return f'Статус запроса - {resp.status} «Хороший»' 
                case 400:
                    return f'Статус запроса - {resp.status} «Плохой запрос»'
                case 401:
                    return f'Статус запроса - {resp.status} «Unauthorized»'
                case 403:
                    return f'Статус запроса - {resp.status} «Forbidden»'
                case 404:
                    return f'Статус запроса - {resp.status} «Не найдено»'
                case _:
                    return f'Статус запроса - {resp.status} None'
                