class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next=None
class Linkedlist:
    def __init__(self) -> None:
        self.head = None
        self.tail= None
    
    def add_end(self,value):
        new_node =Node(value)
        if self.head is None:
            self.head=new_node
            self.tail = new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    
    def remove_end(self):
        if self.head is None:
            return
        else:
            cur = self.head
            pre = None
            while cur.next:
                pre = cur
                cur = cur.next
            pre.next = None
            self.tail = pre
    def add_begin(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head =new_node
            self.tail= new_node
        else:
            new_node.next=self.head
            self.head = new_node
    def remove_begin(self):
        if self.head is None:
            return
        else:
            cur = self.head
            self.head = self.head.next
            cur.next=None
    
    def __str__(self) -> str:
        res=""
        cur = self.head
        while cur:
            res+= str(cur.value) +" <-"
            cur=cur.next
        return res
a= Linkedlist()
a.add_end(5)
a.add_end(6)
a.add_end(7)
print(a)
print(f"{a} <- None")
a.add_begin(2)
a.add_begin(1)
print(a)
a.remove_end()
print(a)
a.remove_begin()
print(a)