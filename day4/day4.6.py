list=list(range(1000))
j=0
for i in range(len(list)):
    if list[j]%2==1:
        list.pop(j)
    else:
        j+=1
print(list)