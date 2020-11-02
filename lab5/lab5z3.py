# Перевірити справедливість рівності при задй точності Є
# ln(x)=2+[(x-1/x+1)+1/3*(x-1/x+1)**3+...+1/2n-1*(x-1/x+1)**2n-1+...]
# x>0

from math import log
eps = float(input("Епсилон = "))
x = float(input("x = "))
e = 2.718281828
a = log(x, e)
if x>0:
    n=1
    s=0
    b=1/(2*n-1)*((x-1/x+1)**(2*n-1))
    while abs(b)>eps:
        k=1/(2*n-1)
        b=k*((x-1/x+1)**k)
        s+=b
        n+=1
    else:
        s+=2
else:
    print("Error")
if a==s:
    print("Рівність справедлива")
else:
    print("Рівність несправедлива")