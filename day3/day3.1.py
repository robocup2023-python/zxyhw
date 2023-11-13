def peach(n):
    if n==10:
        return 1
    return 2*(peach(n+1)+1)
total=peach(1)
print('%d'%total)