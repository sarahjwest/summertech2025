def pal(word):
    if len(word)-1==0:
        print("pal")
    elif word[0]!= word[len(word)-1]:
        print("not pal")
    else:
        pal(word[1:-1])
pal("ddddddddddd")