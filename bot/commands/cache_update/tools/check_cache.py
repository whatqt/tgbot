from .lessen import connection



async def check(id_group, day):
    tgbot = connection["tgbot"]
    current_schedule = tgbot[id_group]
    _class = await current_schedule.find_one(
        {"_id": id_group}
    )
    return _class[day]
            


