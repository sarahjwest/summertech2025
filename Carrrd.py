class card:
    def __init__(self,suit,v):
        self.suit = suit
        self.v=v
    def __str__(self):
        if self.v==11:
            return("Jack of "+self.suit)
        elif self.v==12:
            return ("Queen of "+self.suit)
        elif self.v == 13:
            return ("King of "+self.suit)
        elif self.v == 1:
            return ("Ace of "+self.suit)
        else:
            return (str(self.v)+" of "+self.suit)
    def __repr__(self):
        return str(self)