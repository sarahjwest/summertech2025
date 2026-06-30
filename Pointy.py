class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def gitx(self):
        return self.x
    def gity(self):
        return self.y
    def setx (self,newx):
        self.x=newx
    def sety (self,newy):
        self.y=newy
    def __str__(self):
        return str(self.x)+" "+str(self.y)
    