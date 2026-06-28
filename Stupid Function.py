def Shape (x,y):
    return (x*y)
Shape (455555550,5)
print (Shape(20, 20))
width =  int(input("What is the width"))
length = int(input("What is the length"))
print (Shape(width,length))


def fc (x):
    return ((x-32)*(5/9))
far = float(input("What is the fehrenheit?"))
print ("The celsius is "+ str(fc(far)))

def cf (x):
    return (x*1.8 +32)
cell = float(input("What is the celcius?"))
print ("The Fahrenheit is"+str(cf(cell)))
