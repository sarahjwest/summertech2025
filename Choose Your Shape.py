Ch = input ("What shape do you want? T = traiangle, D = diamond, P = parallegram, E = eye, H = holloed out diamond, and X = x.")
if Ch == "T":
    for j in range (3):
        for k in range (3-j):
            print (" ",end= "")
        for i in range (j+1):
            print ("* ",end = "")
        print()
if Ch == "D":
    for j in range (3):
        for k in range (3-j):
            print (" ",end= "")
        for i in range (j+1):
            print ("* ",end = "")
        print()
    for o in range (3):
        for s in range (o+1):
            print (" ",end= "")
        for w in range (3-o):
            print ("* ",end = "")
        print()
if Ch == "P":
    for j in range (3):
        for k in range (3-j):
            print (" ",end= "")
        for i in range (4):
            print ("* ",end = "")
        for y in range (j + j):
            print (" ",end = "")
        for f in range (4):
            print ("* ",end = "")
        print()
if Ch == "E":
    for j in range (3):
        for k in range (3-j):
            print (" ",end= "")
        for i in range (4):
            print ("* ",end = "")
        for y in range (j + j):
            print (" ",end = "")
        for f in range (4):
            print ("* ",end = "")
        print()
    for o in range (3):
        for c in range (1+o):
            print (" ",end= "")
        for b in range (4):
            print ("* ",end = "")
        for q in range(2-o):
            print (" ", end = "")
        for s in range (2-o):
            print (" ", end = "")
        for b in range (4):
            print ("* ",end = "")
        print()
if Ch == "H":
    for j in range (3):
        for k in range (3-j):
            print (" ",end= "")
        for i in range (1):
            print ("* ",end = "")
        for y in range (j + j):
            print (" ",end = "")
        for f in range (1):
            print ("* ",end = "")
        print()
    for o in range (3):
        for c in range (1+o):
            print (" ",end= "")
        for b in range (1):
            print ("* ",end = "")
        for q in range(2-o):
            print (" ", end = "")
        for s in range (2-o):
            print (" ", end = "")
        for b in range (1):
            print ("* ",end = "")
        print()
if Ch == "X":
    for o in range (3):
        for c in range (1+o):
            print (" ",end= "")
        for b in range (1):
            print ("* ",end = "")
        for q in range(2-o):
            print (" ", end = "")
        for s in range (2-o):
            print (" ", end = "")
        for b in range (1):
            print ("* ",end = "")
        print()
    for j in range (3):
        for k in range (3-j):
            print (" ",end= "")
        for i in range (1):
            print ("* ",end = "")
        for y in range (j + j):
            print (" ",end = "")
        for f in range (1):
            print ("* ",end = "")
        print()