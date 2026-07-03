Toes= [["_ ","_ ","_ "],["_ ","_ ","_ "],["_ ","_ ","_ "],]
mark= ("X ")
feet = True
t=0
while feet == True:
    for i in range (0,3):
        for j in range (0,3):
            print (Toes [i][j],end = "")
        print (" ")


    
    Ticks1 = int( input ("Choose a row 0, 1, or 2"))
    Tacks1 = int (input ("Choose a column 0, 1, or 2"))
    t=t+1
    while Toes [Ticks1][Tacks1] != ("_ "):
        print ("You cannot put somthing there!")
        Ticks1 = int( input ("Choose a row 0, 1, or 2"))
        Tacks1 = int (input ("Choose a column 0, 1, or 2"))
    Toes [Ticks1][Tacks1] = mark

    if Toes[0][0]== mark and Toes[1][0]== mark and Toes[2][0] == mark:
        print ("You win:)")
        feet = False
    elif Toes[0][1]== mark and Toes[1][1]== mark and Toes[2][1] == mark:
        print ("You win:)")
        feet = False
    elif Toes[0][2]== mark and Toes[1][2]== mark and Toes[2][2] == mark:
        print ("You win:)")
        feet = False
    elif Toes[0][0]== mark and Toes[0][1]== mark and Toes[0][2] == mark:
        print ("You win:)")
        feet = False
    elif Toes[1][0]== mark and Toes[1][1]== mark and Toes[1][2] == mark:
        print ("You win:)")
        feet = False
    elif Toes[2][0]== mark and Toes[2][1]== mark and Toes[2][2] == mark:
        print ("You win:)")
        feet = False
    elif Toes[0][0]== mark and Toes[1][1]== mark and Toes[2][2] == mark:
        print ("You win:)")
        feet = False
    elif Toes[0][2]== mark and Toes[1][1]== mark and Toes[2][0] == mark:
        print ("You win")
        feet = False
    elif t == 9:
        print("Tie. Did you think anyone was gonna win? Its ticks tacks and toes!")
        feet = False
    elif mark == "X ":
        mark = ("O ")
    elif mark == "O ":
        mark = ("X ")