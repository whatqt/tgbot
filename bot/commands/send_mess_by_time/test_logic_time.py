import datetime

# Текущее время
now = datetime.datetime.now()

# Определенное время (например, 22:00)
target_time = now.replace(hour=21, minute=35, second=0, microsecond=0)

# Если текущее время уже после указанного (например, 22:00), добавим день
if now > target_time:
    target_time += datetime.timedelta(days=1)

# Разница во времени
time_difference = target_time - now

# Переводим в секунды
seconds_until_target = int(time_difference.total_seconds())

print(f"Время в секундах до 22:00: {seconds_until_target}")
