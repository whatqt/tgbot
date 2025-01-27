from pymongo import MongoClient



connection = MongoClient("localhost", 27017)
tgbot = connection["tgbot"]
schedules = [
    "schedule_1008",
    "schedule_1014",
    "schedule_1010",
    "schedule_1005",
    "schedule_1006",
    "schedule_1011",
    "schedule_1007",
    "schedule_1013",
    "schedule_1004",
    "schedule_1009",
    "schedule_992",
    "schedule_987",
    "schedule_988",
    "schedule_994",
    "schedule_991",
    "schedule_990",
    "schedule_993",
    "schedule_977",
    "schedule_979",
    "schedule_976",
    "schedule_978",
    "schedule_981",
    "schedule_1016",
    "schedule_1022",
    "schedule_1020",
    "schedule_1021",
    "schedule_1017",
    "schedule_1018",
    "schedule_1026",
    "schedule_1025",
    "schedule_1019",
    "schedule_1024"
]

dict_schedule = {
    "monday_one": [],
    "tuesday_one": [],
    "wednesday_one": [],
    "thursday_one": [],
    "friday_one": [],
    "saturday_one": [],
    "monday_two": [],
    "tuesday_two": [],
    "wednesday_two": [],
    "thursday_two": [],
    "friday_two": [],
    "saturday_two": [],
    "exams": {}
}

for schedule in schedules:
    # tgbot.create_collection(
    #     schedule
    # )
    current_schedule = tgbot[schedule]
    dict_schedule["_id"] = schedule
    current_schedule.insert_one(dict_schedule)

    print(f"{schedule} is create!")