# За даними дійсними числами a і b  обчислити
# u = f(a,b)+f(2,a)+2
# де f(x,y) = { x**3+sqrt(x**2+y**4), якщо x>y
#             { (x**2-2*x+sqrt(x))/5sqrt(x**3) , в інших випадках.

from math import sqrt

def f(x, y):
    if x>y:
        return x**3+sqrt(x**2+y**4)
    else:
        return (x**2-2*x+sqrt(x))/(x**3/5)

a = float(input("a = "))
b = float(input("b = "))
u = f(a, b)+f(2, a)+2
print(f"u = {u}")