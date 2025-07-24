rep=True
while rep== True:
    num1= int(input ("Put a number here."))
    num2= int(input ("Put a number here."))
    op1= input ("Put a operation here.")
    if op1== "+":
        print(num1 + num2) 
    if op1 == "-":
        print(num1-num2)
    if op1 == "*":
        print(num1*num2)
    if op1 == "/":
        print (num1//num2)
    muti = input ("do you want to go again?")
    if muti == "no":
        rep = False
        print ("Thanks for playing.")