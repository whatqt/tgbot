def generator_schedule():
    ranges = {
        1: schedule_1008,2: schedule_1014, 3: schedule_1010,               
        4: schedule_1005, 5: schedule_1006, 6: schedule_1011,              
        7: schedule_1007, 8: schedule_1013, 9: schedule_1004,               
        10: schedule_1009, 11: schedule_992, 12: schedule_987,               
        13: schedule_988, 14: schedule_994, 15: schedule_991,
        16: schedule_989, 17: schedule_990, 18: schedule_993,
        19: schedule_977, 20: schedule_984, 21: schedule_979,
        22: schedule_976, 23: schedule_982, 24: schedule_983,
        25: schedule_978, 26: schedule_981, 27: schedule_937,
        28: schedule_940, 29: schedule_936, 30: schedule_930,
        31: schedule_919, 32: schedule_933 
    }

    my_shedule = range(1, 33)

    for i in my_shedule:
        yield ranges[i]
    
def generator_id():
    ranges = {
        1: '1008', 2: '1014', 3: '1010',
        4: '1005', 5: '1006', 6: '1011',
        7: '1007', 8: '1013', 9: '1004',
        10: '1009', 11: '992', 12: '987',
        13: '988', 14: '994', 15: '991',
        16: '989', 17: '990', 18: '993',
        19: '977', 20: '984', 21: '979',
        22: '976', 23: '982', 24: '983',
        25: '978', 26: '981', 27: '937',
        28: '940', 29: '936', 30: '930',
        31: '919', 32: '933'
    }
    
    my_id = range(1,33)
    for i in my_id:
        yield ranges[i]


currentday_dict = {
    0: 'monday',
    1: 'tuesday',
    2: 'wednesday',
    3: 'thursday',
    4: 'friday',
    5: 'saturday',
    6: None
}

#Так как redis нет на Windows, а WSL у меня не работает, а место под вторую операционку нет, то приходится выкручиваться таким образом
schedule_1008 = {
    'monday_one': '', 
    'tuesday_one': '', 
    'wednesday_one': '', 
    'thursday_one': '', 
    'friday_one': '', 
    'saturday_one': '',
    'monday_two': '', 
    'tuesday_two': '', 
    'wednesday_two': '', 
    'thursday_two': '', 
    'friday_two': '', 
    'saturday_two': ''
}

schedule_1014 = {
    'monday_one': '', 
    'tuesday_one': '', 
    'wednesday_one': '', 
    'thursday_one': '', 
    'friday_one': '', 
    'saturday_one': '',
    'monday_two': '', 
    'tuesday_two': '', 
    'wednesday_two': '', 
    'thursday_two': '', 
    'friday_two': '', 
    'saturday_two': ''
}

schedule_1010 = {
    'monday_one': '', 
    'tuesday_one': '', 
    'wednesday_one': '', 
    'thursday_one': '', 
    'friday_one': '', 
    'saturday_one': '',
    'monday_two': '', 
    'tuesday_two': '', 
    'wednesday_two': '', 
    'thursday_two': '', 
    'friday_two': '', 
    'saturday_two': ''    
}

schedule_1005 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_1006 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_1011 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_1007 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_1013 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_1004 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_1009 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_992 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_987 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_988 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_994 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_991 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_989 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_990 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_993 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_977 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_984 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_979 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_976 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_982 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_983 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_978 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_981 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_937 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_940 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_936 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_930 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_919 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}

schedule_933 = {
    'monday_one': '',
    'tuesday_one': '',
    'wednesday_one': '',
    'thursday_one': '',
    'friday_one': '',
    'saturday_one': '',
    'monday_two': '',
    'tuesday_two': '',
    'wednesday_two': '',
    'thursday_two': '',
    'friday_two': '',
    'saturday_two': ''
}