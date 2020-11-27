# Дана цілочислова прямокутна матриця.
# Визначити максимальне із чисел, яке зустрічається в даній матриці більше одного разу.

from random import randint
n=int(input("Кількість рядків: "))
m=int(input("Кількість стовпців: "))
matrix = [[randint(-100, 100) for j in range(m)] for i in range(n)]
print(matrix)

d = 0
while d<1:
    maxElement = matrix[0][0]
    for row in matrix:
        for element in row:
            if element > maxElement:
                maxElement = element
    b=0
    for row in matrix:
        for element in row:
            if element == maxElement:
                b+=1
    if b >= 2:
        d+=1
        print(f"Максимальне число яке зустрічається більше одного разу = {maxElement}")
    elif b == 1:
        for row in matrix:
            for element in row:
                if element == maxElement:
                    row.remove(element)
