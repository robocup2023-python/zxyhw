a=[10,9,6]
n=len(a)
end=a[len(a)-1]
c=int(input())
if c < end:
    d=a[:n+1]+[c]+a[n+1:]
else:
    for i in range(n):
        if a[i]<c:
            break
    d=a[:i]+[c]+a[i:]
print(d)