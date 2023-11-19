import random,shutil
n=int(input())
with open('text.txt','w') as f:
    for i in range(n):
        for j in range(random.randint(0,100)):
            f.write(chr(random.randint(32,127)))
        f.write('\n')
f.close()
shutil.copy('text.txt','copy_text.txt')
