F=[0,1]
for i in range(2,20):
    F.append(F[i-2]+F[i-1])
for j in range(0,20):
    print('%d '%F[j])