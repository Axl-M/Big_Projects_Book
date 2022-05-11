description = '''
Глубокая пещера
Динамическое изображение глубокой пещеры, ведущей до самого центра Земли.
'''

import random, sys, time

# КОНСТАНТЫ
WIDTH = 70
PAUSE_AMOUNT = 0.05

print(description)
print('\n Нажмите "Ctrl + C" для выхода.')
time.sleep(3)

leftWidth = 20  # колличество "#" слева от пещеры
gapWidth = 10   # коллличество пробелов (ширина пещеры)

while True:
    # отобразить фрагмент туннеля
    rightWidth = WIDTH - leftWidth - gapWidth   # чтобы ширина строки была постоянной
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))

    # проверяем не нажато ли Ctrl + C во время короткой паузы
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    # подборка ширины левой части
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1
    if diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1
    else:
        pass

    # подбираем ширину пещеры (если нам нужен этот код)
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and gapWidth > 1:
       gapWidth = gapWidth - 1
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
       gapWidth = gapWidth + 1
    else:
       pass  # Ничего не делаем; ширина зазора не меняется.
