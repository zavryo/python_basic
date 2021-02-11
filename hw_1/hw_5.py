"""6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:

1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

"""

start_distance = float(input("Please, enter a distance in a first day:\n"))
distance = float(input("Please, enter a distance in a last day:\n"))

current_distance = start_distance

day = 1

while current_distance < distance:
    print(f'{day}-й день: {current_distance:.2f}')
    day += 1
    current_distance *= 1.1
else:
    print(f'{day}-й день: {current_distance:.2f}')

print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {distance:.2f} км.')
