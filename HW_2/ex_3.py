# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм
# SHUFFLE не использовать! Реализовать свой метод
import random
from random import randint as rnd

size = int(input('Введите размер списка:'))
my_list = []
for i in range(size):
    my_list.append(rnd(0, 100))
print(f'Исходный список:\n {my_list}')

new_list = my_list
for i in range(size):
    rnd_index = rnd(0, size - 1)
    temp = new_list[i]
    new_list[i] = new_list[rnd_index]
    new_list[rnd_index] = temp
print(f'Перемешанный список:\n {new_list} ')


