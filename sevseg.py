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
    number = str(numbers).zfill(minWidth)
    print(number)


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