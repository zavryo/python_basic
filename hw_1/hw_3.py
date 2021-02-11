"""4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

while True:
    try:
        number = int(input("Please, enter number:\n"))
    except ValueError:
        print("Not an integer")
        continue

    if number <= 0:
        print("An number suppose 2b above zero")
        continue

    init_number = number
    max_digit = 0

    while number // 10:
        if number % 10 > max_digit:
            max_digit = number % 10
        if max_digit == 9:
            break
        number //= 10
    else:
        if number % 10 > max_digit:
            max_digit = number % 10

    print(f"The biggest digit in '{init_number}' is {max_digit}")
