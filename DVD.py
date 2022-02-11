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
    pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:   # при нажатии CTRL + C завершить выполнение
        print()
        print('Отскакивающий DVD-логотип')
        sys.exit()