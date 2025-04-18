import sys
sys.path.append('...')
import aiohttp
from bs4 import BeautifulSoup
from aiohttp.client_exceptions import ClientConnectorError



URL = 'https://www.rubinst.ru/schedule'
tables = {'first_week_1': '', 'first_week_2': '',  'second_week_1': '', 'second_week_2': '', 'table_first_schedule': '', 'table_second_schedule': ''}


class ManageParser:

    def __init__(self):
        ...

    async def get_html_schedule(
            self, 
            id_group,
            tables
        ):

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    url=URL, 
                    cookies={'Group': id_group}
                ) as resp:
                    soup = BeautifulSoup(await resp.read(), 'lxml')
                    tables['table_first_schedule'] = soup.find('table', class_="schedule-table")
                    tables['table_second_schedule'] = soup.find(
                        'table', class_="schedule-table"
                    ).find_next('table', class_="schedule-table")
                    #Первая неделя
                    tables['first_week_1'] = tables['table_first_schedule'].find_all(
                        'tr', class_="odd"
                    )
                    tables['first_week_2'] = tables['table_first_schedule'].find_all(
                        'tr', class_="even"
                    )
                    #Вторая неделя
                    tables['second_week_1'] = tables['table_second_schedule'].find_all(
                        'tr', class_="odd"
                    )
                    tables['second_week_2'] = tables['table_second_schedule'].find_all(
                        'tr', class_="even"
                    )
            except ClientConnectorError: 
                return False
            
    async def __get_len_tables(
            self, 
            tables_one, 
            tables_two
        ):

        return len(tables_one)+len(tables_two)
    
    async def __save_text_schedule(self, 
            table, element_list, 
            day, new_list
        ):

        score = 0
        for i in table[element_list]:
            info = i.get_text('th') 
            new_info = info.replace('th', ' ')   
            if score == day:
                new_list.append(new_info)
                break

            score+=1
    
    async def html_result_group_week(
            self, 
            week_one: str, week_two: str,
            day:int, new_list:list,
        ):

        score = 1
        len_tables = await self.__get_len_tables(
            tables[week_one], tables[week_two]
        )
        match len_tables:
                case 4:
                    while score <= 4:
                        match score:
                            case 1:
                                await self.__save_text_schedule(
                                    tables[week_one], 0, day, new_list
                                )
                            case 2:
                                await self.__save_text_schedule(
                                    tables[week_two], 0, day, new_list
                                )
                            case 3:
                                await self.__save_text_schedule(
                                    tables[week_one], 1, day, new_list
                                )
                            case 4:
                                await self.__save_text_schedule(
                                    tables[week_two], 1, day, new_list
                                )
                        score+=1
                case 3:
                    while score <= 3:
                        match score:
                            case 1:
                                await self.__save_text_schedule(
                                    tables[week_one], 0, day, new_list
                                )
                            case 2:
                                await self.__save_text_schedule(
                                    tables[week_two], 0, day, new_list
                                )
                            case 3:
                                await self.__save_text_schedule(
                                    tables[week_one], 1, day, new_list
                                )
                        score+=1
                case 5:
                    while score <= 5:
                        match score:
                            case 1:
                                await self.__save_text_schedule(
                                    tables[week_one], 0, day, new_list
                                )
                            case 2:
                                await self.__save_text_schedule(
                                    tables[week_two], 0, day, new_list
                                )
                            case 3:
                                await self.__save_text_schedule(
                                    tables[week_one], 1, day, new_list
                                )
                            case 4:
                                await self.__save_text_schedule(
                                    tables[week_two], 1, day, new_list
                                )
                            case 5:
                                await self.__save_text_schedule(
                                    tables[week_one], 2, day, new_list
                                )
                        score+=1