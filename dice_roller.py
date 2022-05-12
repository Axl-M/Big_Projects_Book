"""
 === Выбрасыватель игральных костей ===
 Моделирует выбрасывание костей, в нотации Dungeons & Dragons и других настольных ролевых
игр, используются специальные игральные кости с 4, 8, 10, 12 или даже 20 гранями.
В этих играх есть также специальные обозначения для бросков различных костей.
Например, 3d6 означает выбрасывание трех шестигранных костей, а 1d10+2 — выбрасывание
одной десятигранной кости с добавлением к броску бонуса в два очка.
"""
import random
import sys

print('''       Dice Roller, 
Enter what kind and how many dice to roll. The format is the number of
dice, followed by "d", followed by the number of sides the dice have.
You can also add a plus or minus adjustment.

Examples:
  3d6 rolls three 6-sided dice
  1d10+2 rolls one 10-sided die, and adds 2
  2d38-1 rolls two 38-sided die, and subtracts 1
  Q (QUIT) quits the program
=======================================================================
Введите какого типа кость бросить и сколько раз.

Формат: 
    сколько костей, потом "d", затем сколько сторон она имеет.
    также можно добавить/отнять бонус/штраф.

ПРИМЕРЫ:
    3d6 - бросить 3 6-гранных кубика
    1d10+2  - бросить одну 1-гранную кость и добавить 2 бонуса
    2d38-1 - бросить две 38-гранных кости и отнять 1 штрафа.
    Q (QUIT) для выхода.
''')

while True:
    try:
        diceStr = input(' ==> ')
        if diceStr.upper() == 'Q':
            print('\n Bye.......\n Пока......q')
            sys.exit()

        # очищаем строку описания игральных костей (убираем пробелы если они есть)
        # Clean up the dice string:
        diceStr = diceStr.lower().replace(' ', '')
        # ищем "d" в строке описания
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Отсутствует символ "d".   (Missing the "d" character.)')
        # выясняем количество костей (число перед 'd')
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Пропущено количество костей. (Missing the number of dice.)')
        numberOfDice = int(numberOfDice)

        # Выясняем, присутствует ли модификатор в виде знака плюс или минус:
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        # Выясняем количество граней ("6" в "3d6+1"):
        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1:]
        else:
            numberOfSides = diceStr[dIndex + 1: modIndex]
        if not numberOfSides.isdecimal():
            raise Exception('Пропущено количество сторон. (Missing the number of sides.)')
        numberOfSides = int(numberOfSides)

        # Выясняем числовое значение модификатора ( "1" in "3d6+1"):
        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1:])
            if diceStr[modIndex] == '-':
                # Меняем числовое значение модификатора на отрицательное:
                modAmount = -modAmount

        # Моделируем бросок игральных костей:
        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)

        # Отображаем итоговую сумму очков:
        print('Итого:', sum(rolls) + modAmount, '(Выпали кости: ', end='')
        # print('\nTotal:', sum(rolls) + modAmount, '(Each die: ', end='')

        # Отображаем отдельные броски:
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        # Отображаем числовое значение модификатора:
        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(', {}{}'.format(modSign, abs(modAmount)), end='')
        print(')')

    except Exception as exc:
        # Перехватываем все исключения и отображаем сообщение пользователю:
        print('Неправильный ввод. Введите что-то подобное "3d6" или "1d10+2".')
        print('Ввод был некорректен по причине: ' + str(exc), '\n')
        print('Invalid input. Enter something like "3d6" or "1d10+2".')
        print('Input was invalid because: ' + str(exc), '\n')
        continue  # Возвращаемся к приглашению ввести описание игральных костей.
