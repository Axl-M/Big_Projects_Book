description ="""
    == Разложение на множители ==
Находит все множители заданного числа

Множители (factors) заданного числа — другие два числа, произведение которых дает это заданное число.
Например, 2 × 13 = 26, так что 2 и 13 — множители (factors) числа 26. Кроме того, 1 × 26 = 26, так 
что 1 и 26 — также множители 26. Следовательно, у 26 четыре множителя (factors): 1, 2, 13 и 26.
Число, у которого только два множителя: 1 и оно само, называется простым (prime number).
В противном случае оно называется составным (composite number).
(простые числа всегда заканчиваются на нечетную цифру, но не 5.)

Можете ли вы найти простые числа?
"""

import math, sys

print(description)

while True:
    print('Введите положительное целое число для разложения его на множители или Q для выхода.')
    response = input(' ==> ')
    if response.upper() == 'Q':
        print('Exiting........\nBye.......')
        sys.exit()

    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors = []

    # поиск множителей
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0: # нет остатка - множитель
            factors.append(i)
            factors.append(number // i)

    # избавиться от повторов
    factors = list(set(factors))
    factors.sort()

    prime_number = False
    if len(factors) == 2:
        prime_number = True

    # вывод результата
    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    if prime_number:
        print("ЭТО ПРОСТОЕ ЧИСЛО.\nThan's prime number")
    print(', '.join(factors))





