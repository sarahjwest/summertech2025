import random
big_board=[[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "],[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "]]
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
    if d == "h":
        for i in range(l):
            b[row][collum+i]=" * "
    elif d == "v":
        for i in range(l):
            b[row+i][collum]=" * " 
place(3,big_board)
pint(big_board)


    
#hi i like toes.
#do you like toes?
#they are yummy.
#i like to lick them.
#jimmy licks with me.
#he is an expert toe licker.
#