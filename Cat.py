name = input ("What is your name?")
print ("Hello "+ name)
q1= input ("Do you want to go outside? Answer Y or N.")
if q1 == "Y":
    print ("You walk outside and into the yard.")
    q2= input ("Your owner is not home, do you want to run away? Answer Y or N")
    if q2=="Y":
        print ("You climb over the fence.")
        q3= input ("Do you wnat to go north south or west? N, S, or W?")
        if q3 == "N":
            print (" You go north and find a forest.")
            q4 = input ("Do you want to enter? Y or N.")
            if q4 == "Y":
                print ("You find some wild cats that kill you")
            elif q4 == "N":
                print ("A little kid finds you and sticks you in a blender and you die.")
        elif q3 == "S":
            print ("You run into a wolf that eats you")
        elif q3== "W":
            print ("You die to a trap.")
    elif q2 == "N":
        print ("A humman finds you and sticks you in the micorwave and you die.")
elif q1 == "N":
    print ("You die to starvation when your owner never comes and feeds you.")
    