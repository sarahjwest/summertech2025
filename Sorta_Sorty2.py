def medge(l,f,s):
    y=f
    r=(f+s)//2
    Yist = []
    while y < (f+s)//2  and r< s:
        if l[y]> l[r]:
            Yist.append (l[r])
            r=r+1
        else:
            Yist.append (l[y])
            y=y+1
    while y<(f+s)//2:
        Yist.append (l[y])
        y=y+1
    while r<s:
        Yist.append (l[r])
        r=r+1
    for i in range(len(Yist)):
        l[i+f]=Yist[i]
def sorta_medge(l,f,s):
    if s == f+1:
        pass
    else:
        m=(f+s)//2
        sorta_medge(l,f,m)
        sorta_medge(l,m,s)
        medge(l,f,s)
if __name__== "__main__":
    Yist=[1,3,22,4,4,6,77,65,4,3223,45,7,89,3,3,6,7,78,8,9,8,66,6,8,9,55,5,-33,-54,-67,-756,6565,4545,6]
    sorta_medge(Yist,0,len(Yist))
    print (Yist)