
class Node:
    def __init__(self,value,next):
        self.value=value
        self.next=next
class LinkList:
    def __init__(self):
        self.head=None
    def append(self):
        c=int(input("What is the new value? "))
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
        for i in range(Index-1):
            v=v.next
        r=v.next
        v.next=v.next.next
        return r.value
    def length(self):
        v=self.head
        c=1
        if v==None:
            return 0
        else:
            while v.next != None:
                v=v.next
                c=c+1
            return c
"""link = LinkList()
link.append()
link.append()
link.append()
for i in range (link.length()):
    h=link.get(i)
    print(h)
d=int(input("What to remove "))
link.remove(d)
for i in range (link.length()):
    h=link.get(i)
    print(h)"""

