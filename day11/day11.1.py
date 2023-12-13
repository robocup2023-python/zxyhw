import threading
import os
for i in range(10):
    path=str(i)+'.txt'
    with open(path,'w+')as file:
        file.write('python')
        file.close()
def rename(n: int) -> None:
    path=str(n)+'.txt'
    new='py'+path
    os.rename(path,new)
for i in range(10):
    s=threading.Thread(target=rename,args=(i, ))
    s.start()