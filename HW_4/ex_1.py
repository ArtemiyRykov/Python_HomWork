# A. Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint as RI

def create_pattern(min: int, max: int) -> dict:
    degree = int(input('Введите степень максимальную многочлена: '))
    equation_pattern = {}
    for key in range(degree, -1, -1):
        value = RI(min, max)
        equation_pattern[key] = value
    return equation_pattern

def decode_equation(equation: dict) -> str:
    new_equation = ''
    first = True
    for (key, value) in equation.items():
        if value != 0:
            if first:
                if value > 0:
                    new_equation += f'{value}*x**{key} '
                else:
                    new_equation += f'-{value * (-1)}*x**{key} '
                first = False
            else:
                if value == 1:
                    if key == 1:
                        new_equation += f'+ x '
                    elif key == 0:
                        new_equation += f'+ 1 '
                    else:
                        new_equation += f'+ x**{key } '
                elif value > 1:
                    if key == 1:
                        new_equation += f'+ {value}*x '
                    elif key == 0:
                        new_equation += f'+ {value} '
                    else:
                        new_equation += f'+ {value}*x**{key} '
                elif value == -1:
                    if key == 1:
                        new_equation += f'- x '
                    elif key == 0:
                        new_equation += f'- 1 '
                    else:
                        new_equation += f'- x**{key} '
                elif value < 1:
                    if key == 1:
                        new_equation += f'- {abs(value)}*x '
                    elif key == 0:
                        new_equation += f'- {abs(value)} '
                    else:
                        new_equation += f'- {abs(value)}*x**{key} '
    return new_equation + '= 0'


def encode_equation(equation: str) -> dict:
    new_equation = []
    equation = equation.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').split(' ')
    for item in equation:
        if not 'x' in item:
            new_equation.append([item, 0])
        else:
            if item.endswith('x'):
                if item == 'x':
                    new_equation.append(['1', '1'])
                elif item == '-x':
                    new_equation.append(['-1', '1'])
                else:
                    new_equation.append((item + '1').split('*x'))
            else:
                if item.startswith('x'):
                    new_equation.append(('1' + item).split('x**'))
                elif item.startswith('-x'):
                    new_equation.append(item.replace('-', '-1').split('x**'))
                else:
                    new_equation.append(item.split('*x**'))
    equation_patter = {}
    for item in new_equation:
        equation_patter[int(item[1])] = int(item[0])
    return equation_patter

first = create_pattern(-100, 100)
sercond = create_pattern(-10, 20)

def equation_addition(first: dict, second: dict) -> dict:
    base = {}
    base.update(first)
    base.update(second)
    for key in base:
        if first.get(key) and second.get(key):
            base[key] = first.get(key) + second.get(key)
        elif first.get(key):
            base[key] = first.get(key)
        else:
            base[key] = second.get(key)
    return dict(sorted(base.items())[::-1])

result = equation_addition(first, sercond)
print(decode_equation(first))
print(decode_equation(sercond))
print(decode_equation(result))
result_txt = decode_equation(result)

with open('equation.txt', 'w') as file:
    file.write(result_txt)