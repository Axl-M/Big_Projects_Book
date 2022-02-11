'''Анимация отскакивающего от краёв логотипа DVD
CTRL+C для выхода
Не меняйте размер окна во время работы программы'''

import sys, random, time

try:
    import bext
except ImportError:
    print('Эта программа требует установленного модуля bext. \n Можно установить командой pip3 install bext')

# задаем константы
WIDTH, HEIGHT = bext.size()
# print(WIDTH, HEIGHT)
# в Windows нельзя вывести символ в последний столбец без дообавления
# автоматически символа новой строки, поэтому уменьшаем нирину на 1
WIDTH -= 1
NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTION = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# ключи для ассоциативных массивов логотипов
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    # генерация логотипов
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                    X: random.randint(1, WIDTH - 4),
                    Y: random.randint(1, HEIGHT - 4),
                    DIR: random.choice(DIRECTION)})
        if logos[-1][X] % 2 == 1:
            # гарантируем что Х четное число, для столкновения с углом
            logos[-1][X] -= 1

    cornerBounces = 0  # посчитать сколько раз логотип столкнулся с углом
    while True:  # основной цикл программы
        for logo in logos:  # обработка всех логотипов в списке
            bext.goto(logo[X], logo[Y])
            print('   ', end='')

            originalDirection = logo[DIR]

            # проверка, не отскакивает ли логотип от угла
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] == UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # если логотип отскакивает от левого края
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] == UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] == DOWN_RIGHT

            # если отскакивает от правого края
            # WIDTH - 3 так как DVD состоит из 3 букв
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] == UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] == DOWN_LEFT

            # если логотип отскакивает от верхнего края
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] == DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] == DOWN_RIGHT

            # если лого отскакивает от нижнего края
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] == UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] == UP_RIGHT

            if logo[DIR] != originalDirection:
                # поменять цвет при отскакивании логотипа
                logo[COLOR] = random.choice(COLORS)

            # перемещение логотипа ( Х меняется на 2 так как в терминале высота символов в 2 раза больше ширины
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1



    # print(logos)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:   # при нажатии CTRL + C завершить выполнение
        print()
        print('Отскакивающий DVD-логотип')
        sys.exit()