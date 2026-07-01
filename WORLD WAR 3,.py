import Dec
d= Dec.dec()
d.shuffle()
p1hand = []
p2hand = []
for i in range (26):
    p1hand.append(d.draw())
for j in range (26):
    p2hand.append(d.draw())
death =  True
while death == True:
    kill = p1hand.pop()
    people = p2hand.pop()
    print ("p1 had "+str(kill))
    print ("p2 had "+str(people))
    if kill.gitvalue()>people.gitvalue():
        print ("p2 win")
    elif kill.gitvalue()<people.gitvalue():
        print ("p1 win")
    elif kill.gitvalue()==people.gitvalue():
        print ("tie")
    if len(p1hand)==0:
        print ("p1 wins the game.")
        death = False
    elif len(p2hand)==0:
        print ("p2 win")
        death = False
