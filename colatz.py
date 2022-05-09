description = '''
Гипотеза Коллатца, называемая также дилеммой 3n + 1, 
— простейшая из нерешенных задач математики. Начиная с числа n, 
следующие члены последовательности формируются в соответствии с тремя правилами.
1. Если n — четное, то следующий член последовательности равен n / 2. 
2. Если n — нечетное, то следующий член равен n * 3 + 1.
3. Если n = 1, то прекращаем. В противном случае повторяем.
Существует (математически не доказанная) гипотеза, что любая такая последовательность завершается 1. 
'''

import sys, time

print(description)
print('\nВведите начальное число (больше 0) или Q - для выхода:')
responce = input(' > ')
if not responce.isdecimal() or responce == '0':
    print('Вы должны ввести целое число больше 0.')
    sys.exit()

n = int(responce)
print(n, end='', flush=True)
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    print(', ' + str(n), end='', flush=True)
    time.sleep(0.2)
print()
