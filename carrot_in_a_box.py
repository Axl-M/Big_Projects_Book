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
input('Когда  ' + p2Name + ' закроет глаза, нажмите ENTER...')
print()

print(p1Name + ' вот что внутри твоего ящика:')
if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print('''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|    __________
 /    ||   /|   /         /|
+---------+ |  +---------+ |
| КРАСНЫЙ | |  | ЗОЛОТОЙ | |
|   ЯЩИК  | /  |   ЯЩИК  | /
+---------+/   +---------+/
 (МОРКОВКА!)''')
    print(playerNames)
else:
    print('''
   _________
  |         |
  |         |
  |_________|    __________
 /         /|   /         /|
+---------+ |  +---------+ |
| КРАСНЫЙ | |  | ЗОЛОТОЙ | |
|   ЯЩИК  | /  |   ЯЩИК  | /
+---------+/   +---------+/
(МОРКОВКИ НЕТ!)''')
    print(playerNames)

input('Нажмите "ENTER" чтобы продолжить...')
print('\n' * 100) # прокрутить 100 строк - очистка экрана
print(p1Name + ' , скажите ' + p2Name + ' открыть глаза.')
input('Нажмите "ENTER" чтобы продолжить...')
print()
print(p1Name + ', скажите "В МОЁМ ЯЩИКЕ ЕСТЬ МОРКОВКА" либо \n "В МОЁМ ЯЩИКЕ НЕТ МОРКОВКИ"')
print()
input('Нажмите "ENTER" чтобы продолжить...')
print()
print(p2Name + ' , хотите обменяться коробками с ' + p1Name + '? YES/NO')

while True:
    responce = input('> ').upper()
    if not (responce.startswith('Y') or responce.startswith('N')):
        print(p2Name + ', введите "YES" или "NO".')
    else:
        break

firstBox = 'КРАСНАЯ '
secondBox = 'ЗОЛОТАЯ'

if responce.startswith('Y'):
    carrotInFirstBox = not carrotInFirstBox
    firstBox, secondBox = secondBox, firstBox

print(''' ВОТ ВАШИ КОРОБКИ
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |''')
print(f'| {firstBox} | |  | {secondBox}| |')
print('''| КОРОБКА | /  | КОРОБКА | /
+---------+/   +---------+/''')
print(playerNames)
