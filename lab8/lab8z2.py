# Використовуючи підпрограму для знаходження скалярного добутку, обчислити значення виразу:
# s=2<a,b>-3<a,c>, де a,b,c Є R**n
#  <x,y> – скалярний добуток векторів.

def Skal(x, y, n):
    d = 0
    for i in range(n):
        m = x[i]*y[i]
        d+=m
    return d

n = int(input("n = "))
a = []
for i in range(n):
    element = float(input(f"a{i + 1} = "))
    a.append(element)

b = []
for i in range(n):
    element = float(input(f"b{i + 1} = "))
    b.append(element)

c = []
for i in range(n):
    element = float(input(f"c{i + 1} = "))
    c.append(element)

z1 = Skal(a, b, n)
z2 = Skal(a, c, n)
s = (2*z1)-(3*z2)
print(f"Результат виразу s = {s}")





