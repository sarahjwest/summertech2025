Toes= [["_ ","_ ","_ "],["_ ","_ ","_ "],["_ ","_ ","_ "],]
mark= ("X ")
feet = True
while feet == True:
    for i in range (0,3):
        for j in range (0,3):
            print (Toes [i][j],end = "")
        print (" ")

    
    Ticks1 = int( input ("Choose a row 0, 1, or 2"))
    Tacks1 = int (input ("Choose a column 0, 1, or 2"))
    while Toes [Ticks1][Tacks1] != ("_ "):
        print ("you cannot put somthing there.")
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
        print ("You win:)")
        feet = False
    if mark == "X ":
        mark = ("O ")
    elif mark == "O ":
        mark = ("X ")