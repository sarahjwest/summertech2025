import Carrrd
import random
import Sorta_Sorty
class dec:
    def __init__(self):
        self.dec=[]
        for i in range (1,14):
            self.dec.append(Carrrd.card("clubs",i))
            self.dec.append(Carrrd.card("hearts",i))
            self.dec.append(Carrrd.card("spades",i))
            self.dec.append(Carrrd.card("diamonds",i))
    def __str__(self):
        return str(self.dec)
    def shuffle(self):
        for i in range (len(self.dec)):
            Sorta_Sorty.swop (self.dec,i,random.randint(i,len(self.dec)-1))

        