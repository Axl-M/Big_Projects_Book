"""             == Утята ==
Экранная заставка со множеством утят

   >" )   =^^)    (``=   ("=  >")    ("=
   (  >)  (  ^)  (v  )  (^ )  ( >)  (v )
    ^ ^    ^ ^    ^ ^    ^^    ^^    ^^
Программа создает перемещающийся вверх фон с утятами.
Они незначительно отличаются друг от друга: смотрят влево или вправо,
обладают одним из двух размеров тела, четырех типов глаз, двух разновидностей
ртов и трех положений крыльев. В результате получается 96 возможных
вариантов утят, непрерывно выводимых программой
"""

import random, sys, time, shutil

PAUSE = 0.2
DENSITY = 0.10  # 0.0 - 1.0

DUCKLING_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

# Получаем размер окна терминала:
WIDTH = shutil.get_terminal_size()[0]
# В Windows нельзя вывести что-либо в последнем столбце без добавления
# автоматически символа новой строки, поэтому уменьшаем ширину на 1:
WIDTH -= 1

def main():
    print('Ctrl + C to QUIT')



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()