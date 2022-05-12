import random
import time

description = '''
Выбрасывает от 2 до 6 игральных костей, сумму очков на которых вы должны вычислить так быстро, как только можете.
Выпавшие верхние (лицевые) стороны костей отображаются в случайных местах на экране.

Арифметика с игральными костями
Игра с обучающими карточками на сложение, в которой нужно суммировать все очки на выброшенных игральных костях.
За 30 секунд необходимо дать как можно больше ответов.
За каждый правильный ответ начисляется 4 балла.
За каждый неправильный - отнимается 1 балл.
'''

# константы
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3  # -3 чтобы было куда вывести сумму внизу
QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6
REWARD = 4
PENALTY = 1

# Если все кости не помещаются на экране, программа зависает:
assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('''
Арифметика с игральными костями
Игра с обучающими карточками на сложение, в которой нужно суммировать все очки на выброшенных игральных костях.
За {} секунд необходимо дать как можно больше ответов.
За каждый правильный ответ начисляется {} балла.
За каждый неправильный - отнимается {} балл.
'''.format(QUIZ_DURATION, REWARD, PENALTY))
# input('Press Enter to begin...')

correctAnswer = 0
incorrectAnswer = 0
start_time = time.time()

while time.time() < start_time + QUIZ_DURATION:  # основной цикл
    sumAnswer = 0
    diceFaces = []
    # выбрать кость для отображения
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        # die[0] содержит список лицевых сторон костей в виде строк:
        diceFaces.append(die[0])
        # die[1] содержит количество точек на лицевой стороне в виде чисел:
        sumAnswer += die[1]

    # print('die[0]')
    # print(die[0])
    # print('die[1]')
    # print(die[1])
    # print('diceFaces')
    # print(diceFaces)
    # print(sumAnswer)

    # Содержит кортежи (x, y) с местоположением верхнего левого угла кости.
    topLeftDiceCorners = []

    # Определяем, где должна быть размещена кость:
    for i in range(len(diceFaces)):
        while True:
            # Находим случайное место на холсте для размещения кости:
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            # Получаем координаты x, y всех четырех углов:
            #      left
            #      v
            # top >+-------+ ^
            #      | O     | |
            #      |   O   | DICE_HEIGHT (5)
            #      |     O | |
            #      +-------+ v
            #      <------->
            #      DICE_WIDTH (9)
            topLeftX = left
            topLeftY = top
            topRightX = left + DICE_WIDTH
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT

            # Проверяем, не пересекается ли эта игральная кость с предыдущей.
            overlaps = False
            for prevDieLeft, prevDieTop in topLeftDiceCorners:
                prevDieRight = prevDieLeft + DICE_WIDTH
                prevDieBottom = prevDieTop + DICE_HEIGHT
                # Проверяем все углы этой кости, не входят ли они
                # в область, занимаемую предыдущей костью:
                for cornerX, cornerY in ((topLeftX, topLeftY),
                                         (topRightX, topRightY),
                                         (bottomLeftX, bottomLeftY),
                                         (bottomRightX, bottomRightY)):
                    if (prevDieLeft <= cornerX < prevDieRight
                            and prevDieTop <= cornerY < prevDieBottom):
                        overlaps = True
            if not overlaps:
                # Если не пересекается, можем ее тут разместить:
                topLeftDiceCorners.append((left, top))
                break

    # отрисовка кости на холсте
    # ключи - кортежи (х, у) целочисленных значений,
    # значения - символы на соответствующем месте холста
    canvas = {}
    # проходим в цикле по всем костям
    for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
        # проходим в цикле по всем символам лицевой стороны кости
        dieFace = diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                # копируем символ в соответствующее место холста
                canvasX = dieLeft + dx
                canvasY = dieTop + dy
                # в dieFace, списке строковых значений, х и у поменяны местами
                canvas[(canvasX, canvasY)] = dieFace[dy][dx]

    # вывод холста на экран
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')  # незанятое пространство заполнить пробелами ' '
        print()

    # даем игроку возможность ввести свой ответ
    response = input('Введите сумму: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correctAnswer += 1
    else:
        print('Неверно, правильный ответ - ', sumAnswer)
        time.sleep(2)
        incorrectAnswer += 1

# отображаем счет
score = (correctAnswer * REWARD) - (incorrectAnswer * PENALTY)
print('Правильных ответов: ', correctAnswer)
print('Неправильных ответов: ', incorrectAnswer)
print('Счёт:', score)
