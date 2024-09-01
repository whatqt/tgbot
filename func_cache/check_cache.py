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
                'schedule_990': cache.schedule_990[day],
                'schedule_993': cache.schedule_993[day],
                'schedule_977': cache.schedule_977[day],
                'schedule_979': cache.schedule_979[day],
                'schedule_976': cache.schedule_976[day],
                'schedule_978': cache.schedule_978[day],
                'schedule_981': cache.schedule_981[day],
                'schedule_1016': cache.schedule_1016[day],
                'schedule_1022': cache.schedule_1022[day],
                'schedule_1020': cache.schedule_1020[day],
                'schedule_1021': cache.schedule_1021[day],
                'schedule_1017': cache.schedule_1017[day],
                'schedule_1018': cache.schedule_1018[day],
                'schedule_1026': cache.schedule_1026[day],
                'schedule_1025': cache.schedule_1025[day],
                'schedule_1019': cache.schedule_1019[day],
                'schedule_1024': cache.schedule_1024[day]
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
                'schedule_990': cache.schedule_990,
                'schedule_993': cache.schedule_993,
                'schedule_977': cache.schedule_977,
                'schedule_979': cache.schedule_979,
                'schedule_976': cache.schedule_976,
                'schedule_978': cache.schedule_978,
                'schedule_981': cache.schedule_981,
                'schedule_1016': cache.schedule_1016,
                'schedule_1022': cache.schedule_1022,
                'schedule_1020': cache.schedule_1020,
                'schedule_1021': cache.schedule_1021,
                'schedule_1017': cache.schedule_1017,
                'schedule_1018': cache.schedule_1018,
                'schedule_1026': cache.schedule_1026,
                'schedule_1025': cache.schedule_1025,
                'schedule_1019': cache.schedule_1019,
                'schedule_1024': cache.schedule_1024
            }
            
            if id_group in schedules:
                return schedules[id_group]
            


