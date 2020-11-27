# Дана цілочислова квадратна матриця.
# Розмістити елементи парних рядків у порядку зростання.

from random import randint
n=int(input("Кількість рядків і стовпців: "))
matrix = [[randint(0, 9) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i%2 == 0:
            matrix[i].sort()
print(matrix)