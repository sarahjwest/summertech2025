def sert(l):
    if len(l)== 0 or len(l) == 1:
        return l
    else:
        p = l[0]
        s=[]
        b=[]
        for i in range (1,len(l)):
            if l[i]> p:
                b.append (l[i])
            else:
                s.append (l[i])
        s = sert(s)
        b = sert(b)
        return s+[p]+b
if __name__== "__main__":
    Yist = [564,37636,5,674,56,48,57,6]
    Yist = sert (Yist)
    print (Yist)