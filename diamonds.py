description = r'''
Рисует ромбы различного размера
                           /\       /\
                          /  \     //\\
            /\     /\    /    \   ///\\\
           /  \   //\\  /      \ ////\\\\
 /\   /\  /    \ ///\\\ \      / \\\\////
/  \ //\\ \    / \\\///  \    /   \\\///
\  / \\//  \  /   \\//    \  /     \\//
 \/   \/    \/     \/      \/       \/
'''


def main():
    print(description)
    print('\n', '=' * 40)

    # отображение ромбов размерами от 0 до 6
    for diamondSize in range(1, 10):
        display_outline_diamond(diamondSize)
        print()
        display_filled_diamond(diamondSize)


def display_outline_diamond(size):
    # отоброжение верхней половины ромба
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # Пробелы слева.
        print('/', end='')  # Левая сторона ромба.
        print(' ' * (i * 2), end='')  # Внутренность ромба.
        print('\\')  # Правая сторона ромба.)

    # отоброжение нижней половины ромба
    for i in range(size):
        print(' ' * i, end='')  # Пробелы слева.
        print('\\', end='')  # Левая сторона ромба.
        print(' ' * ((size - i - 1) * 2), end='')  # Внутренность ромба.
        print('/')  # Правая сторона ромба.)


def display_filled_diamond(size):
    # отоброжение верхней половины ромба
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # Пробелы слева.
        print('/' * (i + 1), end='')  # Левая сторона ромба.
        print('\\' * (i + 1))  # Правая сторона ромба.
    # Отображает нижнюю половину ромба:
    for i in range(size):
        print(' ' * i, end='')  # Пробелы слева.
        print('\\' * (size - i), end='')  # Левая сторона ромба
        print('/' * (size - i))  # Правая сторона ромба.


if __name__ == '__main__':
    main()
