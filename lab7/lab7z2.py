# Побудувати матрицю А, елементи якої задаються формулою:
# a[ij] = { 1*2*3*4*5*j , якщо i*j= парне.}
#         { 1+2+3+4+5*i , якщо i*j= непарне.}
# i=1,n
# j=1,m
# Побудувати одновимірний масив (переписати матрицю в одновимірний масив).

from math import factorial
n = int(input("Кількість рядків: "))
m = int(input("Кількість стовпців: "))
matrix = []
for i in range(n):
    matrix.append([])
    d = i+1
    for j in range(m):
        c = j+1
        if (d*c)%2 == 0:
            element = factorial(c)
        elif (d*c)%2 != 0:
            element = 0
            for k in range(d+1):
                element = element + k
        matrix[i].append(element)
print(matrix)
