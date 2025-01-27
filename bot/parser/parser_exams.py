import aiohttp
from bs4 import BeautifulSoup
import asyncio


URL = 'https://www.rubinst.ru/schedule'

class GetExams:
    
    async def get_html_exams(
            self,
            id_group: str
        ):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                URL, cookies={"Group": id_group}
                ) as resp:
                print(f"get_exams: {resp.status}")
                soup = BeautifulSoup(await resp.read(), 'lxml')
                try:
                    data_exams = soup.find_all("table", class_="schedule-table")[2]
                except IndexError:
                    return None
                    
                return data_exams
            
    async def get_text_and_return_exams(
            self,
            dates_html_exam,
            all_exams: dict
        ):
            dates_exam = dates_html_exam.find_all("th")
            del dates_exam[0]
            del dates_exam[0]
            del dates_exam[0]
            del dates_exam[0]
            numbers_exams = 0
            # all_exams = {}
            for exam in dates_exam:
                date_exam = exam
                name_exam = date_exam.find_next()
                auditorium_number = name_exam.find_next()
                type_exam = auditorium_number.find_next()      
                numbers_exams+=1
                all_exams["exams"][f"exam_{numbers_exams}"] = {
                    "date": date_exam.text,
                    "name": name_exam.text,
                    "auditorium_number": auditorium_number.text,
                    "type": type_exam.text,
                }
            print(all_exams)
            return all_exams
