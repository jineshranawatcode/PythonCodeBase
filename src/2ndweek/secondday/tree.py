class Node:
    def __init__(self, data) -> None:
        self.data=data
        self.leftChild=None
        self.rightChild=None

    def insert(self,data):
        if data < self.data:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
    
    def print(self,level=0):
        if self.rightChild:
            self.rightChild.print(level+1)
        if self.data != None:
            print(' ' * 4 * level + '->'+ str(self.data))
        if self.leftChild:
            self.leftChild.print(level +1)

root= Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
root.print()