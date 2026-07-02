import random
big_board=[[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "]]
jimmy=[[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "]]
jiggle=[[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "]]
def pint(b):
    for i in range(10):
        for j in range(10):
            print (b [i][j],end = "")
        print (" ")
def place(l,b):
    pint(b)
    print ("The ship length is "+str(l))
    row = int(input("What row would you like to go on?"))
    collum = int(input("What collum would you like to go on?"))
    d = input ("Would you like to place horizontally or vertically?")
    complace(l,b,row,collum,d) 
def complace(l,b,r,c,d):
    if d == "h":
        for i in range(l):
            b[r][c+i]=" * "
    elif d == "v":
        for i in range(l):
            b[r+i][c]=" * " 
def vali(l,b,r,c,d):
    if d=="h":
        volad = True
        for i in range(l,b,r,c,d):
            if r >9 or r<0 or c>9 or c< 0:
                volad =False
            elif b[v][c+i]== " * ":
                volad = False
        return volad
    elif d=="v":
        volad = True
        for i in range(l,b,r,c,d):
            if r >9 or r<0 or c>9 or c< 0:
                volad =False
            elif b[v+i][c]== " * ":
                volad = False
        return volad
    else:
        return False
place(3,big_board)
pint(big_board)
siz = [5,4,3,3,2]
for i in (siz):
    place (i,big_board)
for jgy in (siz):
    complace(jgy,jimmy,random.randint(0,9),random.randint(0,9),random.choice(["h","v"]))




#hi i like toes.
#do you like toes?
#they are yummy.
#i like to lick them.
#jimmy licks with me.
#he is an expert toe licker.
#he knows which toes are the best
#can i have your toes?
#i want your toes.
#give me your toes.
#i will lick them.