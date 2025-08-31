from logic_logs.file.logger import logger
from mongodb.connection import connection



def generator_weekday():
    ranges = {
        1: 'monday_one', 2: 'tuesday_one', 3: 'wednesday_one',
        4: 'thursday_one', 5: 'friday_one', 6: 'saturday_one',
        7: 'monday_two', 8: 'tuesday_two', 9: 'wednesday_two',
        10: 'thursday_two', 11: 'friday_two', 12: 'saturday_two'
    }


    mylist = range(1, 13)
    for i in mylist:
        yield ranges[i]
    
def generator_schedule():
    ranges = {
        1: "schedule_1008", 2: "schedule_1014", 3: "schedule_1010",
        4: "schedule_1005", 5: "schedule_1006", 6: "schedule_1011",
        7: "schedule_1007", 8: "schedule_1013", 9: "schedule_1004",
        10: "schedule_1009", 11: "schedule_992", 12: "schedule_987",
        13: "schedule_988", 14: "schedule_994", 15: "schedule_991",
        16: "schedule_990", 17: "schedule_993", 18: "schedule_977",
        19: "schedule_979", 20: "schedule_976", 21: "schedule_978",
        22: "schedule_981", 23: "schedule_1016", 24: "schedule_1022",
        25: "schedule_1020", 26: "schedule_1021", 27: "schedule_1017",
        28: "schedule_1018", 29: "schedule_1026", 30: "schedule_1025",
        31: "schedule_1019", 32: "schedule_1024", 
        33: "schedule_1027", 34: "schedule_1039", 35: "schedule_1035",
        36:"schedule_1038", 37: "schedule_1028", 38: "schedule_1029",
        39: "schedule_1032",40: "schedule_1030",41: "schedule_1031",
        42: "schedule_1036", 43: "schedule_1037",
    }

    my_shedule = range(1, 44)

    for i in my_shedule:
        yield ranges[i]

async def record_cache_schedule(schedule: str, day_week: str, lst: list):
    global connection
    client_db = connection
    tgbot = client_db["tgbot"]
    current_schedule = tgbot[schedule]

    await current_schedule.update_one(
        {"_id": schedule},
        {"$set": {day_week: lst}}
    )

async def record_cache_exams(schedule_id: str, exams: dict, connection=connection):
    client_db = connection
    tgbot = client_db["tgbot"]
    current_schedule = tgbot[schedule_id]

    await current_schedule.update_one(
        {"_id": schedule_id},
        {"$set": {"exams": exams}}
    )