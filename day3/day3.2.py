for i in range(1,5):
    for j in range(0,5-i):
        print(' ',end='')
    print((2*i-1)*'*')
for i in range(1,4):
    print(' '*(i+1),end='')
    print((7-2*i)*'*')