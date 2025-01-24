from datetime import datetime



class ManageTime:
    def __init__(self, time: str):  
        self.time = time # устанавливает время когда придет уведомление

    async def date(self):
        hour, minute = self.time.split(':')
        date_time = datetime(
            2025, 1, 22, 
            int(hour), 
            int(minute)
        )
        print(date_time)
        return date_time




