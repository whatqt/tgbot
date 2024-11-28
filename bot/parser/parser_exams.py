import aiohttp
from bs4 import BeautifulSoup
import asyncio


URL = 'https://www.rubinst.ru/schedule'

async def get_exams(id_group):
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

async def get_data_exams(data_exams, all_exams):
    dates_exam = data_exams.find_all("th")
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
        all_exams
        all_exams[f"exam_{numbers_exams}"] = {
            "date_exam": date_exam.text,
            "name_exam": name_exam.text,
            "auditorium_number": auditorium_number.text,
            "type_exam": type_exam.text,
        }
    print(all_exams)
    return all_exams

# async def main():
#     data_exams = await get_exams('1016')
#     await get_data_exams(data_exams)


# asyncio.run(main())