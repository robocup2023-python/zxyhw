A=[]
B=[]
C=[[0,0,0],[0,0,0],[0,0,0]]
a=input().split(',')
b=input().split(',')
c=input().split(',')
d=input().split(',')
e=input().split(',')
f=input().split(',')
A.append(a)
A.append(b)
A.append(c)
B.append(d)
B.append(e)
B.append(f)
for i in range(0,3):
    for j in range(0,3):
        C[i][j]=int(A[i][j])+int(B[i][j])
for r in C:
    print(r)