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

        # отработка действий игрока
        print('Ставка:', bet)
        while True:     # выполнять пока игрок не скажет "ХВАТИТ" или не будет перебор
            displayHands(playerHand, dealerHand, False)
            print()

            # проверка на перебор у игрока
            if getHandValue(playerHand) > 21:
                break

            # получить ход игрока: H, S или D
            move = getMove(playerHand, money - bet)

            # обработка действий игрока
            if move == 'D':
                # игрок удваивает, он может увеличить ставку
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f'Ставка увеличена на {bet}')
                print('Ставка:', bet)
            if move in ('H', 'D'):
                # если "ЕЩЁ" или ЭУДВАИВАЮ" игрок берет еще одну карту
                newCard = deck.pop()
                rank, suit = newCard
                print(f'Ваша карта {rank} {suit}')
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    # у игрока ПЕРЕБОР
                    continue
            if move in ('S', 'D'):
                # ХВАТИТ или УДВАИВАЮ - переход хода другому игроку
                break

            # обработка действий ДИЛЕРА
            if getHandValue(playerHand) <= 21:
                while getHandValue(dealerHand) < 17:
                    # дилер берет ещё карту
                    print('КОМПЬЮТЕР делает ход - берет карту.')
                    dealerHand.append(deck.pop())
                    displayHands(playerHand, dealerHand, False)
                    if getHandValue(dealerHand) > 21:
                        break  # перебор
                    input('Нажмите ENTER чтобы продолжить...')
                    print('\n\n')

            # отобразить итоговые карты на руках
            displayHands(playerHand, dealerHand, True)

            playerValue = getHandValue(playerHand)
            dealerValue = getHandValue(dealerHand)
            # проверка ВЫИГРАЛ ПРОИГРАЛ или НИЧЬЯ
            if dealerValue > 21:
                print(f'Вы выиграли $ {bet}')
                money += bet
            elif (playerValue > 21) or (playerValue < dealerValue):
                print('Вы проиграли!')
                money -= bet
            elif playerValue > dealerValue:
                print(f'Вы выиграли $ {bet}')
                money += bet
            elif playerValue == dealerValue:
                print("Ничья! Ставка возвращена.")

            input('Нажмите ENTER для продолжения...')
            print('\n\n')



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


def displayHands(playerHand, dealerHand, showDealerHand):
    '''отображает карты дилера и игрока. Скрыть первую карту дилера если showDealerHand = False'''
    print()
    if showDealerHand:
        print('КОМПЬЮТЕР:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('КОМПЬЮТЕР: ???')
        # скрыть первую карту дилера
        displayCards([BACKSIDE] + dealerHand[1:])

    # показать карты игрока
    print('ИГРОК:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    '''Возвращает стоимость карт '''
    value = 0
    numberOfAces = 0

    # добавить стоимость карты (не туза)
    for card in cards:
        rank = card[0]  # взять из кортежа номинал
        if rank == 'Т':
            numberOfAces += 1
        elif rank in ('В', 'Д', 'К', 'Т'):
            value += 10                     # для фигурных карт
        else:
            value += int(rank)              # для числовых карт

    # добавить стоимость для тузов
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:                # если не перебор ТУЗ = 11
            value += 10

    return value


def displayCards(cards):
    '''Отображает все карты из списка карт'''
    rows = ['', '', '', '', '']         # отоброжаемый в каждой строке текст

    for i, card in enumerate(cards):
        rows[0] += ' ___ '      # верхняя строка карты
        if card == BACKSIDE:    # рубашка карты
            rows[1] +=  '|## | '
            rows[2] +=  '|###| '
            rows[3] +=  '|_##| '
        else:
            # вывод лицевой стороны карты
            rank, suit = card       # карта -кортеж
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # вывести строки на экран
    for row in rows:
        print(row)


def getMove(playerHand, money):
    pass

if __name__ == '__main__':
    main()

