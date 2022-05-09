description = '''
Чо-хан — традиционная игра в кости, распространенная в игорных домах феодальной Японии. 
Две шестигранные игральные кости выбрасываются из чашки, а игроки должны угадать,
окажется сумма четной (чо) или нечетной (хан). Игорный дом берет себе небольшую часть всех выигрышей.
'''

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

print(description)

# денег в наличии
purce = 5000
while 1:    # основной цикл
    # ставка
    print(" У вас есть", purce, "¥. Сколько ставите? (или Q для выхода.)")
    while True: # проверка правильности ставки
        pot = input((' > '))
        if pot.upper() == 'Q':
            print('Спасибо за игру!')
            sys.exit()
        elif not pot.isdecimal():
            print('Необходимо ввести число')
        elif int(pot) > purce:
            print('У вас недостаточно денег для этой ставки.')
        else:
            # допустимая ставка
            pot = int(pot)
            break

    # бросаем кости
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print('На что ставите? С-СНО(чёт) или Н-HAN(нечёт)')
    while True:
        bet = input(' > ').upper()
        if bet != 'C' and bet != 'H':
            print('Введите С или Н ')
            continue
        else:
            break

    # открываем результаты броска костей
    print('Показываем кости:')
    print(' ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print(' ', dice1, '-', dice2)

    # определяем выиграл ли игрок
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctbet = 'C'
    else:
        correctbet = 'H'

    playerWon = bet == correctbet

    # отображаем результат ставки
    if playerWon:
        print('Вы выиграли! Вы получаете', pot, '¥')
        purce += pot
        print('Комиссия игорного дома составляет 10%: ', pot // 10, '¥')
        purce -= pot // 10
    else:   # вычитаем ставку
        purce -= pot
        print('Вы проиграли!')

    # проверяем не закончились ли у игрока деньги
    if purce == 0:
        print('У вас закончились деньги.')
        print('Благодарим за игру')
        sys.exit()