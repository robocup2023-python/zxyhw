import random
f=open('data.txt','w+')
for i in range(100000):
    f.write(str(random.randint(1,100))+'\n')
f.seek(0,0)
print(f.read())
f.close()