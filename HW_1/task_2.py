# 2. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print(f'X | Y | Z   | ¬(X ⋁ Y ⋁ Z) | ¬X ⋀ ¬Y ⋀ ¬Z')
for x in range(0 , 2):
    for y in range(0, 2):
        for z in range(0, 2):
            statement1 = not(x or y or z)
            statement2 = not x and not y and not z
            print(f'{x} | {y} | {z}   |  {statement1}         |{statement2}')