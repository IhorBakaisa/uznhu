# Побудувати масив A=(a[i]), елементи якого складються за формулою
# a[i]=a[i-2]+(a[i-1]/(2**(i-1)))*a[i-3]     i=(4,5...n)
# a[1]=a[2]=x;   a[3]=y
# х,у ввести з клавіатури
# Вивести кількість елементів масиву A, які більші за задане число z.

x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
n = int(input("Кількість елементів A: "))
k=0
A = [x, x, y]
for i in range(3, n):
    A.append(A[i-2]+(A[i-1]/(2**(i-1))*A[i-3]))
for i in range(0, n):
    if A[i]>z:
        k+=1
    else:
        k=k
print(f"Кількість елементів масиву A,які більші за z = {k}")