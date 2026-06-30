import Sorta_Sorty
import Sorta_Sorty2
import Sorta_Sorty3
import random
liiist=[]
for i in range (10000):
    liiist.append (random.randint(-10000,10000000000000))
print ("Bubble sort.")
Sorta_Sorty.sorty(liiist)

liiist=[]
for i in range (10000):
    liiist.append (random.randint(-10000,10000000000000))
print("Merge sort")
Sorta_Sorty2.sorta_medge(liiist,0,len(liiist))

liiist=[]
for i in range (10000):
    liiist.append (random.randint(-10000,10000000000000))
print ("Quick sort")
liiist = Sorta_Sorty3.sert(liiist)
