# -*- coding: utf-8 -*-
instruction = '''
Дедуктивная логическая игра «Бейглз» необходимо по подсказкам угадать секретное число из трех цифр. 
В ответ на ваши попытки угадать игра выдает одну из трех подсказок: 
Pico - если вы угадали правильную цифру на неправильном месте, 
Fermi - если в вашей догадке есть правильная цифра на правильном месте, 
Bagels - если в догадке не содержится правильных цифр. 
На угадывание секретного числа у вас десять попыток.
'''

import random

NUM_DIGITS = 3 # из какого количества цифр состоит задуманное число
MAX_GUESSES = 10 # кол-во попыток

def main():
    print(instruction)

    while True:
        secretNum = getSecretNum()
        print(f'Я загадал  {NUM_DIGITS}-значное число. У вас {MAX_GUESSES} попыток')
        numGuesses = 1

        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Попытка #{numGuesses}')
                guess = input('>')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # число угадано
            if numGuesses > MAX_GUESSES:
                print('У вас закончились попытки.')
                print(f'Было загадано число {secretNum}')

        print('Хотите играть ещё? (Да/Нет) ')
        if not input('>').lower().startswith('д'):
            break
    print('Благодарю за игру!')


def getSecretNum():
    '''Возвращает строку из уникальных случайных цифр'''
    numbers = list('0123456789')
    random.shuffle(numbers) # перетасовать
    # Берем первые цифры для нашего случайного числа
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    '''Возвращает строку подсказку для полученной на входе пары из догадки и секретного числа'''
    if guess == secretNum:
        return 'Вы угадали!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # правильная цифра на правильном месте
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # правильная цифра на НЕправильном месте
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # правильных цифр нет вообще
    else:
        # сортируем подсказки по алфавиту чтобы порядок ничего не выдал
        clues.sort()
        # склеиваем подсказки в одну строку
        return ' '.join(clues)


if __name__ == '__main__':
    main()

