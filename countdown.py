description = '''
Обратный отсчет.
Отображает динамическое изображение таймера обратного 
отсчета  в виде семисегментного индикатора. 
Для останова нажмите Ctrl+C.
'''

import sys, time, sevseg

# задаем количество времени
secondsLeft = 7265

try:
    # while True:
    print('\n' * 60) # очистка экрана

    # получить часы, минуты, секунды из secondsLeft
    hours = str(secondsLeft // 3600)
    minutes = str((secondsLeft % 3600) // 60)
    seconds = str(secondsLeft % 60)

    print(hours, minutes, seconds)

except KeyboardInterrupt:
    sys.exit()
# sevseg.getSevSegStr('9 23.99', 7)
