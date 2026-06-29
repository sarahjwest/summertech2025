
def Searchy (l,s,b,v):
    if s >= b:
        if l[s]==v:
            return s
        else:
            return -1
    else:
        guess = (s+b)//2
        if l[guess]==v:
            return guess
        elif l[guess]>v:
            return Searchy (l=l,s=s,b=guess-1,v=v)
        elif l[guess]<v:
           return Searchy (l=l,b=b,s=guess+1,v=v)
            
num = None
listy = []
th = int(input("What number to search for?"))
while num != "stop":
    num = (input("enter a number "))
    if num != "stop":
        listy.append (int(num))
listy = sorted(listy)
print (Searchy(v=th,s=0,b=len(listy)-1,l=listy))