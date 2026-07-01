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
    def add(self,tt):
        return point(self.gitx()+tt.gitx(),self.gity()+tt.gity())
    def sub (self, aa):
        return point(self.gitx()-aa.gitx(),self.gity()-aa.gity())
    def scale (self, jj):
        return point (self.gitx()*jj,self.gity()*jj)
    def divide(self,dd):
        return(self.scale(1/dd))