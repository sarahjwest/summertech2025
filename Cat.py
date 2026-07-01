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
                q5 = input ("You find some wild cats that say they can teach you how to hunt? Answer Y or N")
                if q5 == "N":
                    q6=input("You are starving, should you look for hummans?Answer Y or N")
                    if q6 == "Y":
                        print ("You find hummans that stick you in a washing machine and you die.")
                    elif q6 == "N":
                        print ("You starve.")
                    else:
                        print ("That is not an answer.")
                elif q5 == "Y":
                    print ("You get in a fight with another cat about food and die.")
                else:
                    print ("That is not an answer.")
            elif q4 == "N":
                print ("A little kid finds you and sticks you in a blender and you die.")
            else:
                print ("That is not an answer.")
        elif q3 == "S":
            print ("You run into a wolf that eats you")
        elif q3== "W":
            print ("You die to a trap.")
        else:
            print ("That is not an answer.")
    elif q2 == "N":
        print ("A humman finds you and sticks you in the micorwave and you die.")
    else:
        print ("That is not an answer.")
elif q1 == "N":
    print ("You die to starvation when your owner never comes and feeds you.")
else:
    print ("That is not an answer.")
    