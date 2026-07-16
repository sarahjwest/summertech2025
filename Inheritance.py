class Person:
    def __init__(self,money,age,name):
        self.money=money
        self.age=age
        self.name=name
class Programmer(Person):
    def __init__(self,level,computer,field):
        super.__init__()
        self.level=level
        self.computer=computer
        self.field=field
P=Programmer(None,"Omen",None)
print(P.name)