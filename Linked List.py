
class Node:
    def __init__(self,value,next):
        self.value=value
        self.next=next
class LinkList:
    def __init__(self):
        self.head=None
    def append(self):
        c=int(input("What is the value of Node?"))
        if self.head==None:
            self.head=Node(c,None)
        else:
            v=self.head
            while v.next != None:
                v=v.next
            v.next=Node(c,None)
    def get(self,Index):
        v = self.head
        for i in range(Index):
            v=v.next
        return v.value
    def remove(self,Index):
        v= self.head
        for i in range(Index):
            v=v.next
        