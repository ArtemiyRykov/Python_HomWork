# 4. Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).

number_quarter = int(input('Введите номер четверти от 1 до 4: '))
while number_quarter < 1 or number_quarter > 4:
    print('Всё не так, давай заново')
    number_quarter = int(input('Введите номер четверти от 1 до 4: '))
if number_quarter == 1:
    print(f'Четверть №{number_quarter} находится в координатах x > 0 и y > 0')
elif number_quarter == 2:
    print(f'Четверть №{number_quarter} находится в координатах x < 0 и y > 0')
elif number_quarter == 3:
    print(f'Четверть №{number_quarter} находится в координатах x < 0 и y < 0')
elif number_quarter == 4:
    print(f'Четверть №{number_quarter} находится в координатах x > 0 и y < 0')
