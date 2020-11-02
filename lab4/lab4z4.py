# Дано A,C,N.
# y=cos(A+C+N),якщо A=C=N.
# y=cos(A*C*N),якщо A<C=N.
# y=cos((A+C)*N), якщо A<C<N.
# y=o, в усіх інших випадках.

from math import cos
A = float(input("A = "))
C = float(input("C = "))
N = float(input("N = "))
if A==C and C==N:
    y = cos(A+C+N)
elif A<C and C==N:
    y = cos(A*C*N)
elif A<C and C<N:
    y = cos ((A+C)*N)
else:
    y = 0.0
print(y)