class point():
    def __init__(self,x:float,y:float,z:float) -> None:
        self.x=x
        self.y=y
        self.z=z
        print('创建了point({},{},{})'.format(self.x,self.y,self.z))
        pass
    def __delattr__(self, __name: str) -> None:
        print('删除了point({},{},{})'.format(self.x,self.y,self.z))
        pass
    def __add__(self,other):
        if(type(other)==point):
            raise TypeError('Error')
        if(type(other)==vector):
            return point(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self,other):
        if(type(other)==vector):
            return point(self.x-other.x,self.y-other.y,self.z-other.z)
        if(type(other)==Point):
            return vector(self.x-other.x,self.y-other.y,self.z-other.z)
    def __eq__(self, __value: object) -> bool:
        if(self.x==__value.x and self.y==__value.y and self.z==__value.z):
            return True
        else:
            return False
        pass
    def __lt__(self,other) -> bool:
        m = self.x**2+self.y**2+self.z**2
        n= other.x**2+other.y**2+other.z**2
        if(m<n):
            return True
        else:
            return False
import math
class vector:
    def __init__(self,x:float,y:float,z:float) -> None:
        self.x=x
        self.y=y
        self.z=z
        pass
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y,+self.z+other.z)
    def __sub__(self,other):
        return vector(self.x-other.x,self.y-other.y,self.z-other.z)
    def __eq__(self, __value: object) -> bool:
        if(self.x==__value.x and self.y==__value.y and self.z==__value.z):
            return True
        else:
            return False
        pass
    def __lt__(self,other) -> bool:
        m= self.x**2+self.y**2+self.z**2
        n= other.x**2+other.y**2+other.z**2
        if(m<n):
            return True
        else:
            return False
    def __clo__(self,other):
        h=math.radians(other)
        a=math.sin(h)
        b=math.cos(h)
        return vector(self.x*a-self.y*b,self.x*a+self.y*b,self.z)
    def __atc__(self,other):
        h = math.radians(other)
        a = math.sin(h)
        b = math.cos(h)
        return vector(self.x*a+self.y*b,-self.x*b+self.y*a,self.z)
