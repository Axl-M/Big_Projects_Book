description = """
                    == ДНК ==
Простое динамическое изображение двойной спирали ДНК.
            Нажмите Ctrl+C для останова.
"""

import random, sys, time

PAUSE = 0.15  # 0.5 - 0.0
# Отдельные строки динамического изображения DNA:
ROWS = [
    #123456789 <- Для наглядной оценки количества пробелов:
    '         ##',  # У индекса 0 нет нуклеотидов {}.
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',  # У индекса 9 нет нуклеотидов {}.
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']
#123456789 <- Для наглядной оценки количества пробелов:

try:
    print(description)
    time.sleep(2)
    rowIndex = 0

    while 1:
        # Увеличиваем rowIndex на 1 для отрисовки следующей строки:
        rowIndex += 1
        if rowIndex == len(ROWS):
            rowIndex = 0

        # У строк с индексами 0 и 9 нет нуклеотидов:
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue

        # Выбираем случайные пары оснований гуанин-цитозин и аденин-тимин:
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = 'G', 'C'

        # Выводим строку на экран.
        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(PAUSE)

except KeyboardInterrupt:
    sys.exit()
