# 2. Напишите программу, которая найдёт произведение пар чисел
# списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]
import random

size = int(input('Введите длину списка: '))
my_list = []
for i in range(size):
    my_list.append(random.randint(0, 10))

if len(my_list)%2 == 0:
    length = len(my_list) // 2
else:
    length = len(my_list) // 2 + 1

new_list = []
for i in range(length):
    new_list.append(my_list[i]*my_list[len(my_list)-i-1])
print(f'Созданный список:\n{my_list}\nсписок произведений пар:\n{new_list}')
