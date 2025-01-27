def emoji_number_couple(nubmer: int):
    match nubmer:
        case 1:
            return '1️⃣'
        case 2:
            return '2️⃣'
        case 3:
            return '3️⃣'
        case 4:
            return '4️⃣'
        case 5:
            return '5️⃣'
        
        case _:
            return nubmer

def emoji_time_couple(time: str):
    match time:
        case '8:30-10:00':
            return '🕗'
        case '10:10-11:40':
            return '🕙'
        case '12:10-13:40':
            return '🕛'
        case '13:50-15:20':
            return '🕐'
        case '15:30-17:00':
            return '🕜'
        
        case _:
            return time