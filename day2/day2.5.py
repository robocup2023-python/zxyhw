num=[]
for i in range(101,201):
    k=1
    for j in range(2,i+1):
        if i%j==0:
            k+=1
    if k==2:
        num.append(i)
print(num)