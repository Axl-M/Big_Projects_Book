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

