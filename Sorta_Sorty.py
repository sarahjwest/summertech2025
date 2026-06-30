def swop (l,f,s):
    t = l[f]
    l[f] =l[s]
    l[s]=t
def sorty (l):
    for i in range(0,len(l)):
        for j in range (0,len(l)-1):
            if l[j]> l[j+1]:
             swop(l,j,j+1)
if __name__== "__main__":
    DeYist = [1,3,4,5,2,4,56,1,43,6,2,5,2,4,-54]
    sorty(DeYist)
    print (DeYist)
