import Dec
d= Dec.dec()
d.shuffle()
p1hand = []
p2hand = []
kill = []
people = []
stuff = 0
for i in range (26):
    p1hand.append(d.draw())
for j in range (26):
    p2hand.append(d.draw())
death =  True
while death == True:
    print (str(stuff) + " turns have passed")
    stuff = stuff + 1
    kill.append (p1hand.pop(0))
    people.append(p2hand.pop(0))
    print ("p1 has "+str(len(p1hand)+1)+ " cards")
    print ("p2 has "+str(len(p2hand)+1)+ " cards")
    print ("p1 had "+str(kill))
    print ("p2 had "+str(people))
    killcard= kill[len(kill)-1]
    peoplecard= people[len(people)-1]
    if killcard.gitvalue()>peoplecard.gitvalue():
        print ("p2 win")
        p1hand=p1hand+kill+people
        kill = []
        people = []
    elif killcard.gitvalue()<peoplecard.gitvalue():
        print ("p1 win")
        p2hand= p2hand+kill+people
        kill = []
        people = []
    elif killcard.gitvalue()==peoplecard.gitvalue():
        print ("tie")
        for yy in range (3):
            if len (p1hand)== 0:
                break
            if len(p2hand) == 0:
                break
            kill.append(p1hand.pop(0))
            people.append(p2hand.pop(0))
    if len(p1hand)==0:
        print ("p1 wins the game.")
        death = False
    elif len(p2hand)==0:
        print ("p2 wins the game")
        death = False
    elif stuff == 100_000:
        print ("Stop wasting so much time on war.")
        death = False
