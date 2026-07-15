import Linked_List
class Stack:
    def __init__(self):
        self.link=Linked_List.LinkList()
    def Push(self):
        self.link.append()
    def Pop(self):
        return(self.link.remove(self.link.length()-1))
link = Stack()
link.Push()
link.Push()
link.Push()
for i in range (link.link.length()):
    h=link.link.get(i)
    print(h)
link.Pop()
for i in range (link.link.length()):
    h=link.link.get(i)
    print(h)

    
