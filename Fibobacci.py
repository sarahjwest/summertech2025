def Fib(Pos):
    if Pos==0:
        return 0
    elif Pos==1:
        return 1
    else:
        return(Fib(Pos-1)+Fib(Pos-2))
print(Fib(25))

