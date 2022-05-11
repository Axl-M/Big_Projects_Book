description = '''
Модуль семисегментной индикации
для использования в других программах.
Семисегментный индикатор, сегменты обозначены буквами от A до G:
 __A__
|     |    Все цифры, отображаемые на семисегментном индикаторе:
F     B     __       __   __        __   __  __   __   __
|__G__|    |  |   |  __|  __| |__| |__  |__    | |__| |__|
|     |    |__|   | |__   __|    |  __| |__|   | |__|  __|
E     C
|__D__|
'''

def getSevSegStr(number, minWidth=0):
    """Возвращает строковое значение для цифры на семисегментном индикаторе.
    Если возвращаемое строковое значение меньше minWidth, оно дополняется нулями."""

# Преобразуем число в строковое значение на случай, если это не int или не float:
    number = str(number).zfill(minWidth)
    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.':   # визуализация десятичной точки
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue    # пропускаем место между цифрами
        elif numeral == '-': # выводим знак минуса
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':  # Визуализируем 0.
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':  # Визуализируем 1.
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':  # Визуализируем 2.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':  # Визуализируем 3.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':  # Визуализируем 4.
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':  # Визуализируем 5.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':  # Визуализируем 6.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':  # Визуализируем 7.
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':  # Визуализируем 8.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':  # Визуализируем 9.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'
        # Добавляем пробел (для пространства между цифрами),
        # если эта цифра — не последняя:
        if  i != len(number) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)

    # print(number)
    # print('\n'.join(rows))


if __name__ == '__main__':
    print('This module is meant to be imported rather than run.')
    print('For example, this code:')
    print('    import sevseg')
    print('    myNumber = sevseg.getSevSegStr(42, 3)')
    print('    print(myNumber)')
    print()
    print('...will print 42, zero-padded to three digits:')
    print(' __        __ ')
    print('|  | |__|  __|')
    print('|__|    | |__ ')