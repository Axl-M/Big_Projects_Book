description = '''
Обратный отсчет.
Отображает динамическое изображение таймера обратного 
отсчета  в виде семисегментного индикатора. 
Для останова нажмите Ctrl+C.
'''

import sys, time, sevseg

# задаем количество времени
secondsLeft = int(input('Введите колличество секунд: '))

try:
    while True:
        print('\n' * 60) # очистка экрана

        # получить часы, минуты, секунды из secondsLeft
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)

        # получаем из модуля строковые значения для цифр
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # отображение цифр
        print(hTopRow + '     ' + mTopRow + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

        if secondsLeft == 0:
            print('\n  * * * * * BOOM! * * * * *')
            break

        print('\n Нажмите "Ctrl + C" для выхода.')
        time.sleep(1)
        secondsLeft -= 1

    # print(hours, minutes, seconds)

except KeyboardInterrupt:
    sys.exit()
# sevseg.getSevSegStr('9 23.99', 7)
