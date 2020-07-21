# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ

import random
print('Введите диапазон для целого числа')
min_int = int(input('Введите начало диапазона: '))
max_int = int(input('Введите конец диапазона: '))

print('Введите диапазон для вещественного числа')
min_float = float(input('Введите начало диапазона: '))
max_float = float(input('Введите конец диапазона: '))

print('Введите диапазон для символа')
min_char = str(input('Введите начало диапазона: '))
max_char = str(input('Введите конец диапазона: '))

print('Случайное целое число: ' + str(random.randint(min_int, max_int)))
print('Случайное вещественное число: ' + str(random.uniform(min_float, max_float)))
print('Случайный символ: ' + chr(random.randrange(ord(min_char), ord(max_char))))
