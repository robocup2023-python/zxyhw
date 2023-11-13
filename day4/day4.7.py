n=233
list=[]
count=0
flag=0
num=0
for i in range(n):
    list.append(i+1)
i=0
while count < n-1:
    if list[i]!=0:
        num+=1
    if num==3:
        list[i]=flag
        num=0
        count+=1
    i+=1
    if i==n:
        i=0
for e in list:
    if e!=flag:
        print(e)  