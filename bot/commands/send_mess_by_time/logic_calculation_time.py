from datetime import datetime, timedelta


class CountNextNotification:
    def __init__(self, date_time):
        self.date_time = date_time
    
    async def count(self):
        new_time = datetime.now()
        target_time = new_time.replace(
            hour=self.date_time.hour, 
            minute=self.date_time.minute,
            second=0, microsecond=0
        )

        if new_time > target_time:
            target_time += datetime.timedelta(days=1)

        time_difference = target_time - new_time
        seconds_until_target = int(time_difference.total_seconds())
        
        return seconds_until_target