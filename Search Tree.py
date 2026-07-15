class Node:
    def __init__(self,left,right,value):
        self.left=left
        self.right=right
        self.value=value
class Tree:
    def __init__(self,root):
        self.root=Node(None,None,root)
    def append(self,num):
        c=self.root
        while True:
            if num >= c.value:
                if c.right==None:
                    c.right = Node(None,None,num)
                    break
                else:
                    c=c.right
            elif num < c.value:
                if c.left==None:
                    c.left= Node(None,None,num)
                    break
                else:
                    c=c.left
    def Search(self,num):
        c= self.root
        while True:
            if num > c.value:
                c = c.right
            elif num < c.value:
                c=c.left
            elif num==c.value:
                return True
                break
            elif c==None:
                return False
                break
    def remove(self,num):
        c = self.root
        p=None
        while True:
            if num > c.value:
                p=c
                c=c.right
            elif num< c.value:
                p=c
                c=c.left
            elif c==None:
                break
            elif c.value==num:
                if c.right==None and c.left==None:
                    if p.left == c:
                        p.left= None
                    elif p.right == c:
                        p.right=None
                elif c.right==None:
                    if p.left==c:
                        p.left=c.left
                    elif p.right==c:
                        p.right==c.left
                elif c.left == None:
                    if p.left ==c:
                        p.left=c.right
                    elif p.right==c:
                        p.right=c.right
                else:
                    if p.left==c:
                        p.left=c.right
                        k=c.right
                        while k.left != None:
                            k=k.left
                        k.left=c.left
                    elif p.right ==c:
                        p.right=c.right
                        k=c.right
                        while k.left != None:
                            k=k.left
                        k.left=c.left
t=Tree(3)
for i in range(10):
    g=int(input("What to add to tree"))
    t.append(g)
s=int(input("What to remove"))
t.remove(s)
t.Search(s)
