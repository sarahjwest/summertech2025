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
    lick = True
    pint(b)
    print ("The ship length is "+str(l))
    while lick == True:
        row = int(input("What row would you like to go on?"))
        collum = int(input("What collum would you like to go on?"))
        d = input ("Would you like to place horizontally or vertically?")
        if vali(l,b,row,collum,d):
            complace(l,b,row,collum,d) 
            lick = False
    return(b)
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
        for i in range(l):
            if r >9 or r<0 or c+i>9 or c+i< 0:
                volad =False
            elif b[r][c+i]== " * ":
                volad = False
        return volad
    elif d=="v":
        volad = True
        for i in range(l):
            if r+i >9 or r+i<0 or c>9 or c< 0:
                volad =False
            elif b[r+i][c]== " * ":
                volad = False
        return volad
    else:
        return False
def pow():
    roow = int(input("which row to fire a cannonball at?"))
    cool = int(input ("which collum to fire a cannonball at?"))
    if jimmy[roow][cool] == " * ":
        print("Hit!")
        jiggle[roow][cool]= " ^ "
    elif jimmy[roow][cool]== " _ ":
        print("Miss.")
        jiggle[roow][cool]= " # " 
    pint(jiggle)
def compow(b):
    ghhg=True
    while ghhg == True:
        rooow = random.randint(0,9)
        coool = random.randint(0,9)
        if b[rooow][coool] == " * ":
            print("You got hit:(")
            b[rooow][coool] = " ^ "
            ghhg=False
        elif b[rooow][coool] == " _ ":
            print("The computer missed:)")
            b[rooow][coool]=" # "
            ghhg=False
    pint(big_board)

siz = [5,4,3,3,2]
for i in (siz):
    big_board=place (i,big_board)
for jgy in (siz):
    ugugu = True
    while ugugu == True:
        jog  = random.randint(0,9)
        jag = random.randint(0,9)
        jug = random.choice(["h","v"])
        if vali(jgy,jimmy,jog,jag,jug):
            complace(jgy,jimmy,jog,jag,jug)
            ugugu = False
j =True
while j == True:
    pow()
    g = 0
    for i in (jiggle):
        for a in i:
            if a==" ^ ":
                g=g+1
    if g == 17:
        print ("You win.")
        j=False
        break
    compow(big_board)
    h = False
    for i in (big_board):
        if " * " in i:
            h=True
    if h == False:
        print ("You loose. Haha!")
        j=False

