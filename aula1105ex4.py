from random import randint
v1 = []
v2 = []
v3 = []
for i in range(20):
    v1.append(randint(0,99))
    if v1[i]%10==7:
        v2.append(v1[i])
    else:
        v3.append(v1[i])
print(v1)
print(v2)
print(v3)