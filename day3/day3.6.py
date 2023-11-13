year=int(input())
month=int(input())
day=int(input())
Mon=[31,28,31,30,31,30,31,31,30,31,30,31]
total=0
x=0
for i in range(0,month-1):
    total=total+Mon[i]
if (year%4==0 and year%100!=0)or(year%400==0):
    x=1
if(month>1 and x==1):
    total=total+1
total=total+day
print(total)