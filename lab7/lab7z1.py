# Дана цілочислова прямокутна матриця.
# Визначити суму від’ємних елементів матриці з обома парними індексами.

from random import randint
n=int(input("Кількість рядків: "))
m=int(input("Кількість стовпців: "))
matrix = [[randint(-20, 20) for j in range(m)] for i in range(n)]
print(matrix)

d = 0
for i in range(n):
    for j in range(n):
        if i%2 == 0 and j%2 ==0:
            if matrix[i][j]<0:
                d += matrix[i][j]
print(f"Сума від’ємних елементів матриці з обома парними індексами = {d}")



