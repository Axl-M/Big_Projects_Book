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
print(WIDTH, HEIGHT)