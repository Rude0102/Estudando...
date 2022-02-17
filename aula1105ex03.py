from random import randint
a=[]
b=[]
for i in range(10):
    a.append(randint(1,50))
    b.append(randint(1,50))
print(a)
print(b)
c=[]
for i in range(10):
    c.append(a[i])
    c.append(b[i])
print(c)

