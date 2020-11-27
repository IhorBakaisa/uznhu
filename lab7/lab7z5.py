# Дана цілочислова прямокутна матриця.
# Визначити кількість рядків, які не містять жодного нульового елемента.

from random import randint
n=int(input("Кількість рядків: "))
m=int(input("Кількість стовпців: "))
matrix = [[randint(0, 9) for j in range(m)] for i in range(n)]
print(matrix)

d = 0
for row in matrix:
    k = True
    for element in row:
        if element == 0:
            k = False
            break
    if k:
        d+=1
print(f"Кількість рядків, які не містять жодного нульового елемента = {d}")

