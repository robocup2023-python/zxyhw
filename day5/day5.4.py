import os
import random
import string
def mk():
    os.mkdir("Home:\\robocupzxy\img")
mk()
def g():
    list=random.sample(string.ascii_letters+string.digits,4)
    return "".join(list)
def mkwj():
    os.chdir("Home:\\robocupzxy\img")
    list1=[g() for i in range(100)]
    for name in list1:
        with open(name + ".png","w") as file:
            pass
mkwj()