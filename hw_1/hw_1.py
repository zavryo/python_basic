"""2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
while True:
    try:
        secs = int(input("Please, enter time period in seconds:\n"))
    except ValueError:
        print("Not an integer")
        continue

    if secs < 0:
        print("Time in seconds suppose 2b above zero")
        continue

    h = secs // 3600
    m = (secs - h * 3600) // 60
    # s = secs - h * 3600 - m * 60
    s = secs % 60

    print(f"hh:mm:ss - {h:02}:{m:02}:{s:02}")
