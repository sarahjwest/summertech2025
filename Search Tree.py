class Node:
    def __init__(self,left,right,value):
        self.left=left
        self.right=right
        self.value=value
class Tree:
    def __init__(self,root):
        self.root=root
    def append(self,num):
        c=self.root
        while True:
            if num >= c:
                if c.right==None:
                    c.right = Node(None,None,num)
                    break
                else:
                    c=c.right
            elif num < c:
                if c.left==None:
                    c.left= Node(None,None,num)
                    break
                else:
                    c=c.left
    def Search(self,num):
        c= self.root
        while True:
            if num > c:
                c = c.right
            elif num < c:
                c=c.left
            elif num==c:
                return True
            elif c==None:
                    return False


    
              