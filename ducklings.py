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
    time.sleep(2)

    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)


class Duckling:
    def __init__(self):
        """Создаем нового утенка со случайными отличительными чертами."""
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            # У упитанных утят могут быть только глаза-бусинки.
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])
        self.partToDisplayNext = HEAD

    def getHeadStr(self):
        """Возвращает строковое значение с головой утенка."""
        headStr = ''
        if self.direction == LEFT:
            # Рот:
            if self.mouth == OPEN:
                headStr += '>'
            elif self.mouth == CLOSED:
                headStr += '='

            # Глаза:
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += '" '
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            headStr += ') '  # Затылок.

        if self.direction == RIGHT:
            headStr += ' ('  # Затылок.

            # Глаза:
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += ' "'
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            # Рот:
            if self.mouth == OPEN:
                headStr += '<'
            elif self.mouth == CLOSED:
                headStr += '='

        if self.body == CHUBBY:
            # Дополнительное пустое место, чтобы ширина упитанных
            # и очень упитанных утят совпадала.
            headStr += ' '

        return headStr

    def getBodyStr(self):
        """Возвращает строковое значение с телом утенка."""
        bodyStr = '('  # Левая сторона тела.
        if self.direction == LEFT:
            # Внутреннее пространство тела:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

            # Крыло:
            if self.wing == OUT:
                bodyStr += '>'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

        if self.direction == RIGHT:
            # Крыло:
            if self.wing == OUT:
                bodyStr += '<'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

            # Внутреннее пространство тела:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

        bodyStr += ')'  # Правая сторона тела.

        if self.body == CHUBBY:
            # Дополнительное место, чтобы ширина упитанных и очень
            # упитанных утят совпадала.
            bodyStr += ' '

        return bodyStr

    def getFeetStr(self):
        """Возвращает строковое значение с лапками утенка."""
        if self.body == CHUBBY:
            return ' ^^  '
        elif self.body == VERY_CHUBBY:
            return ' ^ ^ '

    def getNextBodyPart(self):
        """Вызываем соответствующий метод вывода для следующей
        отображаемой части тела утенка. По завершении
        partToDisplayNext задается равной None."""
        if self.partToDisplayNext == HEAD:
            self.partToDisplayNext = BODY
            return self.getHeadStr()
        elif self.partToDisplayNext == BODY:
            self.partToDisplayNext = FEET
            return self.getBodyStr()
        elif self.partToDisplayNext == FEET:
            self.partToDisplayNext = None
            return self.getFeetStr()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()