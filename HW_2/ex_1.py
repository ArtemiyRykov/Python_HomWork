# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# Способ 1

# number = input('Введите число = ')
# suma = 0
# for i in new_number:
#     #print(i)
#     if i.isdigit():
#     suma += int(i)
# print(f'Введенное число {number} сумма цифр данного числа {suma}')

# Способ 2

number = float(input('Введите число = '))
suma = 0
if number < 0: # проверка на отрицательное число
    number *= -1
# print(number)
for i in str(number):
    if i != '.':
        # print(i)
        suma += int(i)
print(f'Введенное число {number} сумма цифр данного числа {suma}')
