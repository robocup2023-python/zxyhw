import os
import random
def xghz():
    files=os.listdir("Home:\\robocupzxy\img")
    for i in range(50):
        k=random.randint(1,50)
        f=files[k]
        p=os.path.splitext(f)
        if p[1]==".png":
            new = p[0]+".jpg"
            os.rename(f,new)
xghz()