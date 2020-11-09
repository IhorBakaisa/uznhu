# Дано два вектори x,y Є R**n.
# Знайти суму векторів.

n = int(input(" n = "))
a = list(map(float, input("Введіть корординати вектора а через пробіл: ").split()))
b = list(map(float, input("Введіть корординати вектора b через пробіл: ").split()))
c = [a[i]+b[i] for i in range(n)]
print(f"Сума векторів = {c}")


# Або за іншим методом

# Дано два вектори x,y Є R**n.
# Знайти суму векторів.

#n=int(input("n = "))
#i=1
#while i<=n:
#    x=int(input(f"x{i} = "))
#    y=int(input(f"y{i} = "))
#    c = int(x) + int(y)
#    print(f"c{i} = " + str(c))
#    i+=1
#else:
#    print("Кінець")