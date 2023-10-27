a=int(input())
n=int(input())
s=0
for i in range(1,n+1):
    s=s+a*10**(n-i)*i
print(s)