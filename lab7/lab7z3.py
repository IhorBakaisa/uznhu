# Створити програму, для знаходження детермінанта квадратної матриці A(2x2).

# 1 Спосіб
matrix = []
print("Введіть матрицю 2 на 2")
n = 2
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
a = 1
b = 1
for i in range(n):
    j=i
    a *= matrix[i][j]
    j = n - 1 - i
    b *= matrix[i][j]
det = a - b
print(f"Детермінант = {det}")

# 2 Спосіб
#matrix = []
#print("Введіть матрицю 2 на 2")
#n = 2
#for i in range(n):
#    row = list(map(int, input().split()))
#    matrix.append(row)
#print(matrix)
#det = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
#print(f"Детермінант = {det}")
