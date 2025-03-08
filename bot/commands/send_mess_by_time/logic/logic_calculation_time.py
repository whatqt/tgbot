from datetime import datetime, timedelta


class CountNextNotification:
    def __init__(self, time: str):
        self.time = time
    
    async def count(self):
        hour, minute = self.time.split(':', 1)
        new_time = datetime.now()
        target_time = new_time.replace(
            hour=int(hour), 
            minute=int(minute),
            second=0, 
            microsecond=0
        )

        if new_time > target_time:
            target_time += timedelta(days=1)

        time_difference = target_time - new_time
        seconds_until_target = int(time_difference.total_seconds())
        
        return seconds_until_target
    