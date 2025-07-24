import random
again= True
while again == True:
    com = random.randint (0,2)
    per = input ("Pick, r,p or s")
    if per == "r" and com == 0:
        print ("Tie")
    elif per == "p" and com== 1:
        print ("Tie")
    elif per == "s" and com== 2:
        print ("Tie")
    elif per == "r" and com == 2:
        print ("Win")
    elif per == "p" and com== 0:
        print ("Win")
    elif per == "s" and com == 1:
        print ("Win")
    elif per =="r" and com == 1:
        print ("Loose")
    elif per == "p" and com ==2:
        print ("Loose")
    elif per == "s" and com == 0:
        print ("Loose")
    ag = input ("do you want to play again?")
    if ag == "no":
        again = False