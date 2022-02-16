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
    calText += 'Понедельник  Втрорник    Среда     Четверг     Пятница   Суббота   Воскресенье   \n'
    # Горизонтальная линия разделитель недель
    weekSeparator = ('+----------' * 7) + '+\n'
    # пустые строки по 10 пробелов между разделителями дней |
    blankRow = ('|          ' * 7) + '|\n'
    # получить первую дату месяца
    currentDate = datetime.date(year, month, 1)
    # отнимаем от currentDate по дню пока не дойдем до воскресенья
    # weekday() для воскресенья возвращает 6 а не 0
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:  # проходим по всем неделям в месяце
        calText += weekSeparator
        # dayNumberRow - строка с метками номеров дней
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)  # переход к следующему дню
        dayNumberRow += '|\n'  # добавить | после субботы
        # добавить строку с номерами дней и 3 пустых строки
        calText += dayNumberRow
        for i in range(3):      # можно заменить кол-во пустых строк
            calText += blankRow

        # проверить закончили обработку месяца?
        if currentDate.month != month:
            break

    # горизонтальная линия в самом низу календаря
    calText += weekSeparator

    return calText


calText = getCalendarFor(year, month)
print(calText)