"""
       === Цифровой поток ===
Экранная заставка в стиле визуальных эффектов фильма "Матрица
"""

import random, shutil, sys, time

MIN_STRING_LENGTH = 6
MAX_STRING_LENGTH = 14
PAUSE = 0.1
STREAM_CHARS = ['0', '1', '#', '@', '.']
# Плотность может варьироваться от 0.0 до 1.0:
DENSITY = 0.02
# Получаем размер окна терминала:
WIDTH = shutil.get_terminal_size()[0]
# В Windows нельзя вывести что-либо в последнем столбце без добавления
# автоматически символа новой строки, поэтому уменьшаем ширину на 1:
WIDTH -= 1

print('Digital Stream')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    # Если для столбца счетчик равен 0, поток не отображается.
    # В противном случае он показывает, сколько раз должны отображаться в этом столбце 1 или 0.
    columns = [0] * WIDTH
    while True:
        # Задаем счетчики для каждого из столбцов:
        for i in range(WIDTH):
            if columns[i] == 0:  # столбец закончился
                if random.random() <= DENSITY:
                    # перезапускаем поток для этого столбца
                    columns[i] = random.randint(MIN_STRING_LENGTH, MAX_STRING_LENGTH)

            # выводим пробел или символ 1/0
            if columns[i] > 0:  # если столбец не закончился
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()  # новая строка в конце троки столбцов
        sys.stdout.flush()  # вывести текст на экран (нужен ли этот код?)
        time.sleep(PAUSE)

except KeyboardInterrupt:
    print('Bye........')
    sys.exit()