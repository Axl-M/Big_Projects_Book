resume = '''
Парадокс дней рождения, также известный как задача о днях рождения, заключается 
в удивительно высокой вероятности того, что у двух человек совпадает день рождения 
даже в относительно небольшой группе людей. В группе из 70 человек вероятность 
совпадения дней рождения у двух людей составляет 99,9 %. Но даже в группе всего 
лишь из 23 человек вероятность совпадения дней рождения составляет 50 %. 
Это не столько парадокс, как удивительный результат.
Приведенная программа производит несколько вероятностных экспериментов, чтобы 
определить процентные соотношения для групп различного размера. Подобные эксперименты 
с определением возможных исходов с помощью множества случайных испытаний называются 
экспериментами Монте-Карло.
'''
import datetime, random

def getBirthdays(numberOfBirthdays):
    '''Возвращает список обьектов дат для случайных дней рождения'''
    birthdays = []
    for i in range(numberOfBirthdays):
        #  год не играет роли, лишь бы в обьектах дней рождения он был одинаковый
        startOfYear = datetime.date(2001, 1, 1)
        # получить случайный день года
        randomNumberOfDay = datetime.timedelta(random.randint(0, 364)) # к-во дней
        birthday = startOfYear + randomNumberOfDay
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    ''' Возвращает обьект даты рождения встречающийся нескольео раз в списке дней рождения'''
    if len(birthdays) == len(set(birthdays)):
        return None  # все даты различны
    #  сравниваение всех ДР друг с другом попарно
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 : ]):
            if birthdayA == birthdayB:
                return birthdayA  # вернуть найденные соответствия

# отображение вводной информации:
print(resume)

# MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
MONTHS = ('Янв', 'Фев', 'Maр', 'Апр', 'Maя', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек')

while True:  # пока пользователь не введет допустимое значение
    print(('Сколько дней рождения сгенерировать? (Мах 100'))
    responce = input('> ')
    if responce.isdecimal() and (0 < int(responce) <= 100):
        numBDays = int(responce)
        break   # введено допустимое значение

print()

# Генерация и отображение дней рождения:
print(f'Здесь  {numBDays} дня рождения:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # вывести запятую для каждого ДР после первого
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = f'{monthName} {birthday.day}'
    print(dateText, end='')
print('\n' * 2)

# Есть ли совпадающие ДР
match = getMatch(birthdays)

# вывод результатов
print('В этой симуляции, ', end='')
if match != None:
    monthName = MONTHS[match.month -1]
    dateText = f'{monthName} {match.day}'
    print('У нескольких людей день рождения ', dateText)
else:
    print('Совпадающие дни рождения отсутствуют.')
print()

# произвести 100 000 операций  имитационного моделирования
print('Генерируем', numBDays, 'случайных дней рождения 100.000 раз...')
input('Нажмите ENTER чтобы начать...')

print('Запустим ещё 100.000 симуляций.')
simMatch = 0 # число операций моделирования с совпадающими днями рождения
for i in range(100_000):
    # отображаем сообщение о ходе выполнения каждые 100_000 операций
    if i % 10_000 == 0:
        print(i, 'симуляций запущено...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100.000 симуляций запущено.')

# вывод результатов имитационного моделирования
probability = round(simMatch / 100_000 * 100, 2)
print('За 100.000 симуляций, из', numBDays, 'людей, имеются совпадающие дни рождения в этой группе', simMatch, 'раз.')
print('Это означает, что', numBDays, 'людей имеют', probability, '% шанс совпадения дня рождения в данной группе.')

