resume = '''
Эта программа генерирует подходящие для распечатки текстовые файлы с 
календарями на выбранный месяц (в выбранном году) и сохраняет в файл'''

import datetime

DAYS = ('Понедельник', 'Втрорник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
MONTH = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
         'Октябрь', 'Ноябрь', 'Декабрь')

print(resume)

while True:
    print('Введите год для календаря:')
    responce = input('> ')
    if responce.isdecimal() and int(responce) > 0:
        year = int(responce)
        break
    print('Введите год в 4-х значном формате, например 2023.')
    continue

while True:
    print('Введите месяц для календаря, 1-12:')
    responce = input('> ')
    if not responce.isdecimal():
        print('Введите номер месяца, например 3 для Марта.')
        continue
    month = int(responce)
    if 1 <= month <= 12:
        break
    print('Введите номер месяца от 1 до 12.')

def getCalendarFor(year, month):
    calText = ''    # содержит строковое значение с календарем
    # Поместить меcяц и год вверху календаря
    calText += (' ' * 34) + MONTH[month - 1] + ' ' + str(year) + '\n'
    # добавить метки дней недели
    calText += ' Понедельник   Втрорник   Среда    Четверг   Пятница   Суббота   Воскресенье   \n'

    return calText


calText = getCalendarFor(year, month)
print(calText)