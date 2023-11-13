import random
import math
f=open('da.txt','w+')
for i in range(10):
    f.write(str(random.randint(100))+str(random.randint(100))+str(random.randint(100)),sep=',')
fd=f.readlines()
a=0
b=0
c=0
for row in fd:
    tmp=row.split(',')
    a=a+tmp[1]
    if(b<tmp[1]):
        b=tmp[1]
    c=tmp[1]
    if(c>tmp[1]):
        c=tmp[1]
d=a/10
print(d)

    
