# Дано текстовий файл, який містить дійсні числа. Визначити найбільший елемент.

file = open("data1.txt", "r")
numbers = list(map(float, file.readline().split()))
file.close()

maxElement = numbers[0]
for element in numbers:
    if element > maxElement:
        maxElement = element
print(f"Максимальний елемент = {maxElement}")
