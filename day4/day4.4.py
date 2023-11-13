n=int(input())
m=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
def ls(arr,n):
    for i in range(n):
        tmp=arr[len(arr)-1]
        for j in range(len(arr)-1):
            arr[len(arr)-1-j]=arr[len(arr)-1-j-1]
        arr[0]=tmp
ls(l,m)
print(l)
