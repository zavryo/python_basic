"""5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).

Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
while True:
    income = float(input("Please, enter company income: \n"))
    exp = float(input("Please, enter company expenses: \n"))

    if income - exp < 0:
        print("A loss occurs")
    elif income - exp > 0:
        print(f"A profit occurs with rent {income / exp}")

        emps = int(input("Please, enter number of employers: \n"))
        print(f"A profit per employer {(income - exp) / emps}")

    else:
        print("Neither profit no loss occurs")


