'''
битовая карта (bitmap) — двумерное изображение, каждый пиксел которого может быть
одного из двух цветов, представлена в виде многострочного строкового значения и
служит для определения способа отображения пользовательского сообщения. В
битовой карте пробелы соответствуют пустому пространству, а все прочие символы
заменяются символами из пользовательского сообщения.
'''

import sys

bitmap = '''
....................................................................
  **************    *  *** **  *       ******************************
  ********************* ** ** *  *   ****************************** *
**      *****************       ******************************
         *************          **  * **** ** ************** *
         *********            *******   **************** * *
         ********           ***************************  *
*        * **** ***         ***************  ******  ** *
            ****  *         ***************    *** ***  *
               ******         *************     **    **  *
                ********        *************      *  ** ***
                ********         ********          * ***  ****
                  *********         ******  *        **** ** * **
                  *********         ****** * *           *** *   *
                 ******          ***** **             *****   *
                 *****            **** *            ********
                 *****             ****              *********
                 ****              **                 *******   *
                 ***                                       *    *
                 **     *                    *
....................................................................
'''


print('Сообщение в виде битовой карты')
print('Введите сообщение для отображения.')
message = input('> ')
if message == '':
    sys.exit()


# пройти в цикле по всем СТРОКАМ битовой карты
for line in bitmap.splitlines():
    # проходим в цикл по всем СИМВОЛАМ строки
    for i, bit in enumerate(line):
        if bit == ' ':
            # вывести пустое пространство сгласно пробелу в битовой карте
            print(' ', end='')
        else:
            # вывести символ из сообщения
            # i увеличивается и при остатке от деления (%) на длину message получаем числа от 0 до длины message
            # таким образом перебираем символы в message постоянно
            print(message[i % len(message)], end='')
    print()     # новая строка