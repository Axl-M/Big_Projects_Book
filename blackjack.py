'''
Блек-джек, известный также как «двадцать одно», — карточная игра,
в которой игроки пытаются набрать количество очков, как можно
более близкое к 21, но не больше.
'''

rules = '''
Попытайтесь набрать как можно больше очков,
но не более 21.
Король, Дама и Валет - 10 очков
Туз - 1 либо 10 очков
Карты от 2 до 10 имеют соответствующее достоинство (2-10)
(H)it - взять ещё карту
(S)tand - прекратить барать карты
При первой игре вы можете (D)ouble - удвоить, чтобы увеличить свою ставку.
но должны взять ещё карту, прежде чем остановиться.
В случае ничьей ставка возвращается игроку.
Раздающий останавливается на 17.
'''

import random, sys

# Задаем значения констант:
HEARTS = chr(9829) # Символ 9829 — '♥'.
DIAMONDS = chr(9830) # Символ 9830 — '♦'.
SPADES = chr(9824) # Символ 9824 — '♠'.
CLUBS = chr(9827) # Символ 9827 — '♣'.
# (Список кодов chr можно найти в https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'

def main():
    print(rules)
    money = 5000
    while True: # основной цикл программы
        if money <= 0: # деньги закончились
            print('Вы проиграли!')
            print('Хорошо что вы не играли на настоящие деньги.')
            print('Благодарю за игру!')
            sys.exit()
        # Игрок делает ставку на раунд
        print('Денег:', money)
        bet = getBet(money)

        # сдаём диллеру и игроку по 2 карты из колоды
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]


        print(dealerHand)
        print(playerHand)


def getBet(maxBet):
    '''Спрашиваем сколько игрок ставит на этот раунд'''
    while True:      # спрашиваем пока не будет введено корректное значение
        print(f'Сколько вы ставите? 1-{maxBet}, или Q-выход')
        # print('Сколько вы ставите? (1-{}, или Q-выход)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'Q':
            print('Благодарю за игру!')
            sys.exit()
        if not bet.isdecimal():
            continue    # игрок не ответил - спрашиваем снова
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDeck():
    '''Возвращает список кортежей (номинал, масть) для всех 52 карт.'''
    deck = []
    for suit in (HEARTS, SPADES, DIAMONDS, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))          # добавить числовые карты
        for rank in ('В', 'Д', 'К', 'Т'):
            deck.append((rank, suit))               # добавить фигурные карты
    random.shuffle(deck)
    return deck

if __name__ == '__main__':
    main()
        
    