"""3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.

10 + 1010 + 101010 = 10 (1 + 101 + 10101)
11 + 1111 + 111111 = 11 (1 + 101 + 10101)

100 + 100100 + 100100100 = 100 (1 + 1001 + 1001001)

"""

while True:
    try:
        number = int(input("Please, enter any number:\n"))
    except ValueError:
        print("Not a number")
        continue

    if number < 0:
        print("A number suppose 2b above zero")
        continue

    solution_1 = number + int(str(number) + str(number)) + int(str(number) + str(number) + str(number))

    n = len(str(number))
    solution_2 = number * (10 ** (2 * n) + 2 * 10 ** n + 3)

    print(f"Expression n + nn + nnn: {solution_1}")
    print(f"Expression n + nn + nnn: {solution_2}")
