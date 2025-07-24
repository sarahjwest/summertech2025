import random
guess= -1
rando= random.randint(1,10)
while guess != rando:
    guess = int(input ("What is your guess?"))
    if guess < rando:
        print ("Too low.")
    if guess > rando:
        print ("Too high.")
print ("Correct")
