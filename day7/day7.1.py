import random
fl=open('data.txt','w')
for i in range(1,11):
    fl.write(str(random.randint(1,10))+','+str(random.randint(1,10))+','+str(random.randint(1,10))+'\n')
fl.close()
ls=[]
with open('data.txt','r') as f:
    l=f.readline()
    while l:
        ls.append(int(l.split(',')[1]))
        l=f.readline()
ls.sort()
avg=sum(ls)/len(ls)
print(avg)
print(ls[-1])
print(ls[0])
print((ls[4]+ls[5])/2)