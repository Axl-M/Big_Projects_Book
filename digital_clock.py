"""      ===  Цифровые часы  ===
 Отображает показывающие текущее время цифровые часы с семисегментным индикатором.
 Нажмите Ctrl+C для останова.
 Требует наличия в том же каталоге файла sevseg.py
"""
import sys
import time
import sevseg

try:
    # while 1:
        # очистка экрана
    print('\n' * 60)
    curentTime = time.localtime()
    print(curentTime)


except KeyboardInterrupt:
    print('Bye.........')
    sys.exit()
