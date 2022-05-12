"""      === Цифровые часы ===
 Отображает показывающие текущее время цифровые часы с семисегментным индикатором.
 Нажмите Ctrl+C для останова.
 Требует наличия в том же каталоге файла sevseg.py
"""
import sys
import time
import sevseg

try:
    while 1:
        # очистка экрана
        print('\n' * 60)
        curentTime = time.localtime()
        # print(curentTime)

        # % 12, поскольку мы используем 12-, а не 24-часовые часы:
        # hours = str(curentTime.tm_hour % 12)
        hours = str(curentTime.tm_hour) # 24 -часовой формат
        # if hours == '0':
        #     hours = '12'  # 12-часовые часы показывают 12:00, а не 00:00.

        minutes = str(curentTime.tm_min)
        seconds = str(curentTime.tm_sec)

        # Получаем из модуля sevseg строковые значения для цифр:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Отображаем цифры:
        print(hTopRow + '     ' + mTopRow + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)
        print()
        print('Press Ctrl-C to quit.')

        # Продолжаем выполнение цикла до перехода на новую секунду:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != curentTime.tm_sec:
                break

except KeyboardInterrupt:
    print('Bye.........')
    sys.exit()
