"""
 Выбрасыватель игральных костей.
 Моделирует выбрасывание костей, в нотации Dungeons & Dragons и других настольных ролевых
играх используются специальные игральные кости с 4, 8, 10, 12 или даже 20 гранями.
В этих играх есть также специальные обозначения для бросков различных костей.
Например, 3d6 означает выбрасывание трех шестигранных костей, а 1d10+2 — выбрасывание
одной десятигранной кости с добавлением к броску бонуса в два очка.
"""
import random
import sys

print('''Dice Roller, 
Введите какого типа кость выбросить и сколько раз.
Формат: сколько костей, потом "d", затем сколько сторон она имеет.
также можно добавить/отнять бонус/штраф.
ПРИМЕРЫ:
3d6 - бросить 3 6-гранных кубика
1d10+2  - бросить одну 1-гранную кость и добавить 2 бонуса
2d38-1 - бросить две 38-гранных кости и отнять 1 штрафа.
Q (QUIT) для выхода.
''')

while True:
    try:
        diceStr = input(' > ')
        if diceStr.upper() == 'Q':
            sys.exit()

        # очищаем строку описания игральных костей
        diceStr = diceStr.lower().replace(' ', '')
        # ищем "d" в строке описания
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Отсутствует символ "d" ')
        # выясняем количество костей (число перед 'd')
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Пропущено количество костей')
        numberOfDice = int(numberOfDice)

        # Выясняем, присутствует ли модификатор в виде знака плюс или минус:
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        # Выясняем количество граней ("6" в "3d6+1"):
        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1 :]
        else:
            numberOfSides = diceStr[dIndex + 1 : modIndex]
        if not numberOfSides.isdecimal():
            raise Exception('Пропущено количество сторон.')
        numberOfSides = int(numberOfSides)

        # Выясняем числовое значение модификатора (The "1" in "3d6+1"):
        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1 :])
            if diceStr[modIndex] == '-':
                # Меняем числовое значение модификатора на отрицательное:
                modAmount = -modAmount
                



