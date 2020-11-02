#Нехай х[0]=1, де x[i]=x[i-1]+2i, де i=1,2,3...
#Знайти x[10]

n=10
f=1
i=1
while i<=n:
    ff=f+(2*i)
    f=ff
    i+=1
else:
    print("Результат = {0}".format(ff))