from handlears.current_day import *



score = 2 # 1 - первая неделя 2 - вторая неделя 

async def chek_week():
    global score
    current_day = CurrentDay()
    match score:
        case 1:
            if await current_day() == 6:
                score+=1
                return await current_day_two(await current_day())
            else:    
                return await current_day_one(await current_day())
        case 2:
            if await current_day() == 6:
                score-=1
                return await current_day_one(await current_day())
            else:
                return await current_day_two(await current_day())
            





