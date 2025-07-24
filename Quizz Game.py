score= 0
color= input ("What is my favorite color?")
if color=="black":
    print ("correct")
    score+=1
else:
    print ("false")    
animal= input ("What is my favorite animal?") 
if animal=="panda":
    print ("correct")
    score+=1
else:
    print("false")   
game= input ("what is my favorite video game?")
if game == "zelda":
    print ("correct")
    score+=1
else:
    print ("false")
food = input ("What is my favorite food?")
if food== "steak":
    print("correct")
    score+=1
else:
    print("false")
print ("Your score is: "+str(score))