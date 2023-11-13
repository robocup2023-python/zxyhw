li=[]
n=int(input())
for i in range(n):
    li.append(int(input()))
def cal(*args):
    num=0
    s=0
    for x in args:
        s+=x
        num+=1
    avg=s/num
    high=[]
    for i in range(len(args)):
        if args[i] >avg:
            high.append(i)
    return avg,high
re=cal(*li)
print(re)