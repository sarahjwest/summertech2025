def thingy(d,s,m,e):
    if d == 0:
        pass
    else:
        thingy (d-1,s,e,m)
        print ("move disk",d," from",s,"to",e,) 
        thingy (d-1,m,s,e)
num = int(input("What is the number of disks?"))
thingy (num,1,2,3)
