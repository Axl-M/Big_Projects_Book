resume = '''
МОРКОВКА В КОРОБКЕ
Это простая несерьезная игра с блефом для ДВУХ игроков.
У каждого игрока есть коробка; в одной из них лежит морковка,
которую хочет заполучить каждый игрок.
Первый заглядывает в свою коробку и говорит второму, есть ли там морковка.
А второй должен решить: меняться коробками или нет (не заглядывая в свою коробку).
'''

import random

print(resume)
input('Нажмите "ENTER" чтобы начать...')

p1Name = input('Первый игрок введите свое имя: ')
p2Name = input('Второй игрок введите свое имя: ')
playerNames = p1Name[:11].center(11) + '    ' + p2Name[:11].center(11)

print('''ВОТ ДВА ЯЩИКА: 
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
| КРАСНЫЙ | |  | ЗОЛОТОЙ | |
|   ЯЩИК  | /  |   ЯЩИК  | /
+---------+/   +---------+/''')

print()
print(playerNames)
print()
print(p1Name + ', ваш ящик КРАСНЫЙ')
print(p2Name + ', ваш ящик ЗОЛОТОЙ')
print()
print(p1Name + ', вы заглянете в ваш ящик.')
print(p2Name.upper() + ', закройте глаза и не подглядывайте!!! ')
print('Когда  ' + p2Name + ' закроет глаза, нажмите ENTER...')
print()

