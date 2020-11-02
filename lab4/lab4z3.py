# Дано A(x1,y1), B(x2,y2), C(x3,y3).
# Визначити чи є цей трикутник виродженим.

from math import sqrt
x1 = float(input("x1 = "))
x2 = float(input("x2 = "))
x3 = float(input("x3 = "))
y1 = float(input("y1 = "))
y2 = float(input("y2 = "))
y3 = float(input("y3 = "))
a = sqrt((x2-x1)**2+(y2-y1)**2)
b = sqrt((x3-x2)**2+(y3-y2)**2)
c = sqrt((x1-x3)**2+(y1-y3)**2)
if a+b>c or a+c>b or b+c>a:
    print("Трикутник вироджений")
else:
    print("Трикутник не вироджений")