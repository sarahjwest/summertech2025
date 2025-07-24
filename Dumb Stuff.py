Sad= [["_ ","_ ","_ ","_ ","_ ","_ ","_ "],["_ ","_ ","_ ","_ ","_ ","_ ","_ "],["_ ","_ ","_ ","_ ","_ ","_ ","_ "],["_ ","_ ","_ ","_ ","_ ","_ ","_ "],["_ ","_ ","_ ","_ ","_ ","_ ","_ "],["_ ","_ ","_ ","_ ","_ ","_ ","_ "]] 
Tree = True
Mark = "X "
while Tree == True:
    for i in range (6):
            for j in range (7):
                print (Sad [i][j],end = "")
            print (" ")
    Bad= int(input ("Which column do you want to go on?"))
    if Sad[5][Bad] == "_ ":
        Sad[5][Bad] = Mark
    elif Sad[4][Bad] == "_ ":
        Sad[4][Bad] = Mark
    elif Sad[3][Bad] == "_ ":
        Sad[3][Bad] = Mark
    elif Sad[2][Bad] == "_ ":
        Sad[2][Bad] = Mark
    elif Sad[1][Bad] == "_ ":
        Sad[1][Bad] = Mark
    elif Sad[0][Bad] == "_ ":
        Sad[0][Bad] = Mark
    
    if Mark == "X ":
        Mark = "O "
    elif Mark == "O ":
        Mark = "X "