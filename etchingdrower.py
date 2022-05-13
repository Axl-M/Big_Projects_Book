"""             == Гравировщик ==
Графическая программа, рисующая непрерывную линию на экране с помощью клавиш WASD.
Создана под влиянием игры "Волшебный экран".
Например, нарисовать фрактальную кривую Гильберта можно с помощью:
SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW
Или даже еще большую фрактальную кривую Гильберта с помощью:
DDSAASSDDWDDSDDWWAAWDDDDSDDWDDDDSAASDDSAAAAWAASSSDDWDDDDSAASDDSAAAAWA
ASAAAAWDDWWAASAAWAASSDDSAASSDDWDDDDSAASDDSAAAAWAASSDDSAASSDDWDDSDDWWA
AWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWAAWDDDDSDDWDDSDDWDDDDSAASDDS
AAAAWAASSDDSAASSDDWDDSDDWWAAWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWA
AWDDDDSDDWWAAWDDWWAASAAWAASSDDSAAAAWAASAAAAWDDWAAWDDDDSDDWWWAASAAAAWD
DWAAWDDDDSDDWDDDDSAASSDDWDDSDDWWAAWDD
"""

import shutil
import sys

# Задаем константы для символов линий:
UP_DOWN_CHAR         = chr(9474)  # Character 9474 is '│'
LEFT_RIGHT_CHAR      = chr(9472)  # Character 9472 is '─'
DOWN_RIGHT_CHAR      = chr(9484)  # Character 9484 is '┌'
DOWN_LEFT_CHAR       = chr(9488)  # Character 9488 is '┐'
UP_RIGHT_CHAR        = chr(9492)  # Character 9492 is '└'
UP_LEFT_CHAR         = chr(9496)  # Character 9496 is '┘'
UP_DOWN_RIGHT_CHAR   = chr(9500)  # Character 9500 is '├'
UP_DOWN_LEFT_CHAR    = chr(9508)  # Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR   = chr(9524)  # Character 9524 is '┴'
CROSS_CHAR           = chr(9532)  # Character 9532 is '┼'

# Получаем размер окна терминала:
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
# В Windows нельзя вывести что-либо в последнем столбце без добавления
# автоматически символа новой строки, поэтому уменьшаем ширину на 1:
CANVAS_WIDTH -= 1
# Оставляем место в нескольких нижних строках для информации о команде.
CANVAS_HEIGHT -= 5

"""Ключи ассоциативного массива canvas представляют собой целочисленные
кортежи (x, y) координат, а значение — набор букв W, A, S, D,
описывающих тип отрисовываемой линии."""
canvas = {}
cursorX = 0
cursorY = 0


def getCanvasString(canvasData, cx, cy):
    """Возвращает многострочное значение рисуемой в canvasData линии."""
    canvasStr = ''

    """canvasData — ассоциативный массив с ключами (x, y) и значениями
    в виде множеств из строк символов 'W', 'A', 'S' и/или 'D',
    описывающих, в каком направлении идет линия в каждой точке xy."""
    for rowNum in range(CANVAS_HEIGHT):
        for columnNum in range(CANVAS_WIDTH):
            if columnNum == cx and rowNum == cy:
                canvasStr += '#'
                continue

            # Добавляем символ линии для данной точки в canvasStr.
            cell = canvasData.get((columnNum, rowNum))
            if cell in ({'W', 'S'}, {'W'}, {'S'}):
                canvasStr += UP_DOWN_CHAR
            elif cell in ({'A', 'D'}, {'A'}, {'D'}):
                canvasStr += LEFT_RIGHT_CHAR
            elif cell == {'S', 'D'}:
                canvasStr += DOWN_RIGHT_CHAR
            elif cell == {'A', 'S'}:
                canvasStr += DOWN_LEFT_CHAR
            elif cell == {'W', 'D'}:
                canvasStr += UP_RIGHT_CHAR
            elif cell == {'W', 'A'}:
                canvasStr += UP_LEFT_CHAR
            elif cell == {'W', 'S', 'D'}:
                canvasStr += UP_DOWN_RIGHT_CHAR
            elif cell == {'W', 'S', 'A'}:
                canvasStr += UP_DOWN_LEFT_CHAR
            elif cell == {'A', 'S', 'D'}:
                canvasStr += DOWN_LEFT_RIGHT_CHAR
            elif cell == {'W', 'A', 'D'}:
                canvasStr += UP_LEFT_RIGHT_CHAR
            elif cell == {'W', 'A', 'S', 'D'}:
                canvasStr += CROSS_CHAR
            elif cell == None:
                canvasStr += ' '
        canvasStr += '\n'  # Добавляем в конце строк символ новой строки.
    return canvasStr


moves = []
while True:  # Основной цикл программы.
    # Отрисовываем линии, исходя из содержащихся в canvas данных:
    print(getCanvasString(canvas, cursorX, cursorY))

    print('WASD кнопки для перемещения, H -помощь, C -очистить, '
          + 'F -сохранить,  Q -выход.')
    response = input(' ==> ').upper()

    if response == 'Q':
        print('Спасибо за игру!')
        sys.exit()
    elif response == 'H':
        print('Используйте W, A, S, и D символы для перемещения курсора')
        print('отрисовки линии за ним после перемещения. Например, ddd')
        print('рисует линию вправо и  sssdddwwwaaa рисует коробку (квадрат).')
        print()
        print('Вы можете сохранить ваш рисунок в файл нажав F.')
        input('Нажмите ENTER для возврата в программу...')
        continue
    elif response == 'C':
        canvas = {}  # Очищаем canvas.
        moves.append('C')  # Записываем движение.
    elif response == 'F':
        # Сохраняем строковое значение с холстом в текстовый файл:
        try:
            print('Введите название файла для сохранения:')
            filename = input(' ==> ')

            # Проверяем, чтобы имя файла оканчивалось на .txt:
            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(getCanvasString(canvas, None, None))
        except:
            print('ERROR: Не получилось сохранить файл.')

    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue  # Игнорируем букву и переходим к следующей.
        moves.append(command)  # Фиксируем данное движение.

        # Первая добавляемая линия должна формировать полную строку:
        if canvas == {}:
            if command in ('W', 'S'):
                # Делаем первую линию горизонтальной:
                canvas[(cursorX, cursorY)] = {'W', 'S'}
            elif command in ('A', 'D'):
                # Делаем первую линию вертикальной:
                canvas[(cursorX, cursorY)] = {'A', 'D'}

        # Обновляем значения x и y:
        if command == 'W' and cursorY > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorY = cursorY - 1
        elif command == 'S' and cursorY < CANVAS_HEIGHT - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorY = cursorY + 1
        elif command == 'A' and cursorX > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorX = cursorX - 1
        elif command == 'D' and cursorX < CANVAS_WIDTH - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorX = cursorX + 1
        else:
            # Если курсор не двигается, чтобы не выйти за пределы холста,
            # то не меняем множество в canvas[(cursorX, cursorY)]
            # canvas[(cursorX, cursorY)].
            continue

        # Если не существует множества для (cursorX, cursorY), добавляем пустое множество:
        if (cursorX, cursorY) not in canvas:
            canvas[(cursorX, cursorY)] = set()


        # Добавляем строку с направлением во множество для этой точки xy:
        if command == 'W':
            canvas[(cursorX, cursorY)].add('S')
        elif command == 'S':
            canvas[(cursorX, cursorY)].add('W')
        elif command == 'A':
            canvas[(cursorX, cursorY)].add('D')
        elif command == 'D':
            canvas[(cursorX, cursorY)].add('A')
