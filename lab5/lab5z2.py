# n Є N
# Алгоритм для визначення кількості цифр в n

n = int(input("n = "))
i = 0
if n==0:
    i+=1
elif n>0:
    while n>0:
        n=n//10
        i+=1
else:
    if n==-1:
        i+=1
    else:
        while n<-1:
            n=n//10
            i+=1

print("Кількість цифр = {0}".format(i))