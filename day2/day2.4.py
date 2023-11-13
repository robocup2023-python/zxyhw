for n in range(100,1000):
    i=n%10
    j=n//10%10
    k=n//100
    if(pow(i,3)+pow(j,3)+pow(k,3)==n):
        print(n)