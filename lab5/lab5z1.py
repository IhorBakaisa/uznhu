# a Є R
# n Є N
# Обчислити a(a+1)...(a+n-1).

a=float(input("a = "))
n=int(input("n = "))
m = 1
i = 1
while n>=i:
    k=a+i-1
    m=m*k
    i+=1
print("Добуток = {0}".format(m))