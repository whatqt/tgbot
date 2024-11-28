import aiohttp
from bs4 import BeautifulSoup
import asyncio


URL = 'https://www.rubinst.ru/schedule'

async def get_exams():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            URL, cookies={"Group": "1008"}
            ) as resp:
            print(resp.status)
            soup = BeautifulSoup(await resp.read(), 'lxml')
            try:
                data_exams = soup.find_all("table", class_="schedule-table")[2]
            except IndexError:
                return None
                
            return data_exams

async def get_data_exams(data_exams):
    # data_exams = await get_exams()
    dates_exam = data_exams.find_all("th")
    del dates_exam[0]
    del dates_exam[0]
    del dates_exam[0]
    del dates_exam[0]
    print(dates_exam)
    all_exams = {}
    numbers_exams = 0
    for exam in dates_exam:
        dates_exam = exam
        name_exams = dates_exam.find_next()
        auditorium_number = name_exams.find_next()
        type_exams = auditorium_number.find_next()      
        numbers_exams+=1
        all_exams[f"exams_{numbers_exams}"] = {
            "dates_exam": dates_exam.text,
            "name_exams": name_exams.text,
            "auditorium_number": auditorium_number.text,
            "type_exams": type_exams.text,
        }
    print(all_exams)
    return all_exams

# async def main():
#     data_exams = await get_exams()
#     await processing_data_exams(data_exams)


# asyncio.run(main())