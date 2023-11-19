import os
for fl in os.listdir('./test'):
    newline=[]
    with open('./test'+f'/{fl}','r+')as f:
        for line in f:
            newline.append(line.replace('python','class'))
        f.seek(0,0)
        f.truncate()
        f.seek(0,0)
        for line in newline:
            f.write(line)