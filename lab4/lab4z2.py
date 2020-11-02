# Дано a,d Є R.
# Чи належать ці числа інтервалу [1;2]U(3;7).

a = float(input("a = "))
b = float(input("b = "))
if 1<=a<=2 and 1<=b<=2 or 3<a<7 and 3<b<7:
    print("Належать")
else:
    print("Неналежать")