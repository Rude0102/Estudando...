from random import randint
l=[]
while len(l) !=10:
    n=randint (1,20)
    if n not in l:
        l.append(n)