class Person:
    def __init__(self,money,age,name):
        self.money=money
        self.age=age
        self.name=name
    def Work(self):
        print("I was fired from my last job.")
class Programmer(Person):
    def __init__(self,money,age,name,level,computer,field):
        super().__init__(money,age,name)
        self.level=level
        self.computer=computer
        self.field=field
    def Work(self):
        super().Work()
        print("I never got a job because I am bad at coding. I never get hired.")
P=Programmer(None,25,"Bob",None,"Omen",None)
print(P.name)
print(P.money)
P.Work()