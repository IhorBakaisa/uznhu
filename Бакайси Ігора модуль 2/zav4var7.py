# Дано текстовий файл, який містить цілі числа (у першому рядку записано кількість елементів, у
# другому через пробіл послідовність цілих чисел). Впорядкувати ці числа у зростаючому порядку.

file = open("data4.txt", "r")
n = int(file.readline())
numbers = list(map(int, file.readline().split()))
file.close()
numbers.sort()
print(f"Кількість елементів = {n}")
print(numbers)
