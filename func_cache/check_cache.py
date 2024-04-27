from func_cache import cache

async def check(id_group, day, mode):
    match mode:
        case 1:
            schedules = {
                'schedule_1008': cache.schedule_1008[day],
                'schedule_1014': cache.schedule_1014[day],
                'schedule_1010': cache.schedule_1010[day],
                'schedule_1005': cache.schedule_1005[day],
                'schedule_1006': cache.schedule_1006[day],
                'schedule_1011': cache.schedule_1011[day],
                'schedule_1007': cache.schedule_1007[day],
                'schedule_1013': cache.schedule_1013[day],
                'schedule_1004': cache.schedule_1004[day],
                'schedule_1009': cache.schedule_1009[day],
                'schedule_992': cache.schedule_992[day],
                'schedule_987': cache.schedule_987[day],
                'schedule_988': cache.schedule_988[day],
                'schedule_994': cache.schedule_994[day],
                'schedule_991': cache.schedule_991[day],
                'schedule_989': cache.schedule_989[day],
                'schedule_990': cache.schedule_990[day],
                'schedule_993': cache.schedule_993[day],
                'schedule_977': cache.schedule_977[day],
                'schedule_984': cache.schedule_984[day],
                'schedule_979': cache.schedule_979[day],
                'schedule_976': cache.schedule_976[day],
                'schedule_982': cache.schedule_982[day],
                'schedule_983': cache.schedule_983[day],
                'schedule_978': cache.schedule_978[day],
                'schedule_981': cache.schedule_981[day],
                'schedule_937': cache.schedule_937[day],
                'schedule_940': cache.schedule_940[day],
                'schedule_936': cache.schedule_936[day],
                'schedule_930': cache.schedule_930[day],
                'schedule_919': cache.schedule_919[day],
                'schedule_933': cache.schedule_933[day],
            }

            if id_group in schedules:
                return schedules[id_group]
            
        case 2:
            schedules = {
            'schedule_1008': cache.schedule_1008,
            'schedule_1014': cache.schedule_1014,
            'schedule_1010': cache.schedule_1010,
            'schedule_1005': cache.schedule_1005,
            'schedule_1006': cache.schedule_1006,
            'schedule_1011': cache.schedule_1011,
            'schedule_1007': cache.schedule_1007,
            'schedule_1013': cache.schedule_1013,
            'schedule_1004': cache.schedule_1004,
            'schedule_1009': cache.schedule_1009,
            'schedule_992': cache.schedule_992,
            'schedule_987': cache.schedule_987,
            'schedule_988': cache.schedule_988,
            'schedule_994': cache.schedule_994,
            'schedule_991': cache.schedule_991,
            'schedule_989': cache.schedule_989,
            'schedule_990': cache.schedule_990,
            'schedule_993': cache.schedule_993,
            'schedule_977': cache.schedule_977,
            'schedule_984': cache.schedule_984,
            'schedule_979': cache.schedule_979,
            'schedule_976': cache.schedule_976,
            'schedule_982': cache.schedule_982,
            'schedule_983': cache.schedule_983,
            'schedule_978': cache.schedule_978,
            'schedule_981': cache.schedule_981,
            'schedule_937': cache.schedule_937,
            'schedule_940': cache.schedule_940,
            'schedule_936': cache.schedule_936,
            'schedule_930': cache.schedule_930,
            'schedule_919': cache.schedule_919,
            'schedule_933': cache.schedule_933
            }

            if id_group in schedules:
                return schedules[id_group]
            


