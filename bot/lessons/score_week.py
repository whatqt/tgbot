from .current_day import *
from datetime import datetime, timedelta
import asyncio


score = 2
score_week = 1 # 1 - первая неделя 2 - вторая неделя 
night = False

async def while_time():
    global night
    global score_week
    global score

    while True:
        print('цикл запущен')
        now = datetime.now()
        midnight = datetime.combine(now.date(), datetime.min.time()) + timedelta(days=1)
        time_to_midnight = (midnight - now).total_seconds()
        print(time_to_midnight)
        await asyncio.sleep(time_to_midnight)
        print(score)
        match score_week:
            case 1:
                print(1)
                score +=1 
                if score == 8:
                    score_week +=1
                    score-= 7
            case 2:
                print(2)
                score +=1 
                if score == 8: #8
                    score_week -=1
                    score-= 7 #7
            
async def week(input_score_week=None):
    global score_week

    if input_score_week:
        match score_week:
            case 1:
                return 'Вторая неделя'
            case 2:
                return 'Первая неделя'
            
    match score_week:
        case 1:
            return 'Первая неделя'
        case 2:
            return 'Вторая неделя'

async def check_week(day_of_the_week=None, input_score_week=None):
    global score
    global score_week
    global night

    if input_score_week:
        match score_week:
            case 1:
                return await current_day_two(0)
            case 2:
                return await current_day_one(0)
                
    match score_week: 
        case 1:
            print('Первая неделя')
            print('score_week', score_week)
            print('score', score)
            print('\n')
            return await current_day_one(day_of_the_week)

        case 2: 
            print('Вторая неделя')
            print('score_week', score_week)
            print('score', score)
            print('\n')
            return await current_day_two(day_of_the_week)
        






