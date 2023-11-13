class person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def printInfo(self):
        print('我叫%s,年龄:%s,性别:%s'%(self.name,self.age,self.sex))

class student(person):
    def __init__(self,name,age,sex,college,banji):
        super().__init__(name.age.sex)
        self.college + college
        self.banji = banji
    def printInfo(self):
        print('我叫%s,年龄:%s,性别:%s,我是%s的%s班的学生'%(self.name,self.age,self.sex,self.college,self.banji))