from handlears.current_day import *
from datetime import datetime



score = 1 # 1 - первая неделя 2 - вторая неделя 
score_week = 2
night = False

async def while_time():
    global night
    while True:
        print('цикл запущен')
        now = datetime.now()
        midnight = datetime.combine(now.date(), datetime.min.time()) + timedelta(days=1)
        time_to_midnight = (midnight - now).total_seconds()
        # time_to_midnight = 1
        print(time_to_midnight)
        if time_to_midnight >= 0:
            night = True
            print(night)
        else:
            await asyncio.sleep(time_to_midnight)
            night = True
            # print(night)
            
async def week():
    global score_week
    match score_week:
        case 1:
            return 'Первая неделя'
        case 2:
            return 'Вторая неделя'

async def check_week():
    global score
    global score_week
    global night
    match score_week:
        case 1:
            print(1)
            if night is True:
                print(f'ночь {night}')
                score +=1 
                night = False
                print(f'ночь {night}\n')
                if score == 8:
                    score_week +=1
                    score-= 7
        case 2:
            print(2)
            if night is True:
                score +=1 
                night = False
                if score == 8:
                    score_week -=1
                    score-= 7
                    
    current_day = CurrentDay()
    print(night)
    match score_week: 
        case 1:
            print('Первая неделя')
            print('score_week', score_week)
            print('score', score)
            print('\n')
            return await current_day_one(await current_day())
             
        case 2:
            print('Вторая неделя')
            print('score_week', score_week)
            print('score', score)
            print('\n')
            return await current_day_two(await current_day())

        
    





