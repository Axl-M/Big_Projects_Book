resume = '''Шифр Цезаря — древний алгоритм шифрования, использовавшийся Юлием Цезарем.
Буквы в нем шифруются путем сдвига их на определенное количество позиций в алфавите.
Дистанция сдвига называется ключом. Например, если ключ равен 3, то A превращается в D,
B — в E, C — в F и т. д. Для расшифровки сообщения необходимо выполнить сдвиг зашифрованных
символов в противоположном направлении. Данная программа позволяет шифровать и расшифровывать
сообщения в соответствии с приведенным алгоритмом.
ПРОГРАММА КАК ШИФРУЕТ ТАК И РАСШИФРОВЫВАЕТ ЗАКОДИРОВАННЫЙ ТЕКСТ'''

try:
    import pyperclip   # для копирования текста в буфер обмена
except ImportError:
    pass    # если библиотека не установлена - ничего не делать

# все возможные символы для шифрования
# SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'

# print(len(SYMBOLS))
print(resume)
print()

while True:
    print('Хотите (e)-зашифровать или (d)-расшифровать?')
    responce = input('> ').lower()
    if responce.startswith('e'):
        mode = 'encrypt'
        break
    elif responce.startswith('d'):
        mode = 'decrypt'
        break
    print('Нужно выбрать (е) или (d)')

while True:     # ввести ключ шифрования
     maxKey = len(SYMBOLS) - 1
     print(f'Введите ключ ( от 0 до {maxKey})')
     response = input('> ').upper()
     if not response.isdecimal():
         continue
     if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# ввести сообщение для шифрования / дешиврования
print(f'Введите сообщение для {mode}')
message = input('> ')

message = message.upper()

translated = ''  # хранит сообщение

# шифруем / расшифровываем каждый символ сообщения
for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)  # получить числовое значение символа
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
    # переход по кругу если число больше длины SYMBOLS или меньше 0
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
    # добавить соответствующий числу символ в translated
        translated += SYMBOLS[num]
    else:
        # просто добавить символ без шифровки
        translated += symbol

# вывод строки на экран
print(translated)

try:
    pyperclip.copy(translated)
    print('Текст скопирован в буфер обмена.')
except:
    pass  # если pyperclip не установлен - ничего не делать
