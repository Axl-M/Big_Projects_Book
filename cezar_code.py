resume = '''Шифр Цезаря — древний алгоритм шифрования, использовавшийся Юлием Цезарем.
Буквы в нем шифруются путем сдвига их на определенное количество позиций в алфавите.
Дистанция сдвига называется ключом. Например, если ключ равен 3, то A превращается в D,
B — в E, C — в F и т. д. Для расшифровки сообщения необходимо выполнить сдвиг зашифрованных
символов в противоположном направлении. Данная программа позволяет шифровать и расшифровывать
сообщения в соответствии с приведенным алгоритмом.
ПРОГРАММА КАК ШИФРУЕТ ТАК И РАСШИФРОВЫВАЕТ ЗАКОДИРОВАННЫЙ ТЕКСТ'''

try:
    import  pyperclip   # для копирования текста в буфер обмена
except ImportError:
    pass    # если библиотека не установлена - ничего не делать

# все возможные символы для шифрования
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
