# Дано n дійсних чисел.
# Знайти середнє арифметичне значення цих чисел.

n=int(input("n = "))
s=0
i=1
while i<=n:
    d=float(input(f"x{i} = "))
    s+=d
    i+=1
else:
    s=s/n
    print("Середнє арифметичне = {0}".format(s))