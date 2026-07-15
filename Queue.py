import Linked_List
class Queue:
    def __init__(self):
        self.link=Linked_List.LinkList()
    def enqueue(self):
        self.link.append()
    def dequeue(self):
        return(self.link.remove(0))

link= Queue()
link.enqueue()
link.enqueue()
link.enqueue()
for i in range(link.link.length()):
    h=link.link.get(i)
    print(h)
link.dequeue()
for i in range(link.link.length()):
    h=link.link.get(i)
    print(h)
