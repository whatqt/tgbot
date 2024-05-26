def generator():
    ranges = {
        1: 'monday_one', 2: 'tuesday_one', 3: 'wednesday_one',
        4: 'thursday_one', 5: 'friday_one', 6: 'saturday_one',
        7: 'monday_two', 8: 'tuesday_two', 9: 'wednesday_two',
        10: 'thursday_two', 11: 'friday_two', 12: 'saturday_two'
    }

    mylist = range(1, 13)
    for i in mylist:
        yield ranges[i]
    
async def record_cache(shedule_id, day_week, lst):
    shedule_id[day_week] = lst

