# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывестив консоль сам список и сумму его элементов.

n = int(input('Введите число: '))
my_list = []
sum = 0
for i in range(n):
    my_list.append(i+((1+1/n)**n))
    sum += my_list[i]

print(f'Список:\n {my_list}\n сумма элементов списка:\n {round(sum,4)} ')