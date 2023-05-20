from datetime import datetime, timedelta

now = datetime.now()  # текущее время
timer = now + timedelta(minutes=30)  # время через 30 минут

# вывод времени через 30 минут
print(timer.strftime("%Y-%m-%d %H:%M:%S"))