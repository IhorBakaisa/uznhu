# Перевірити справедливість рівності при задй точності Є
# ln(x)=2+[(x-1/x+1)+1/3*(x-1/x+1)**3+...+1/2n-1*(x-1/x+1)**2n-1+...]
# x>0

from math import log10
eps = float(input("Епсилон = "))
x = float(input("x = "))
a = log10(x)
if x>0:
    n=1
    s=0
    b=(1/2*n-1)*(x-1/x+1)**2*n-1
    while b>eps:
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