class stack:
    def __init__(self):
        self.items =[]
    def push(self,item):
        self.items.append(item)

    def is_empty(self):
        if not self.items:
            return True
        return False
    def pop(self):
        if not self.is_empty():
            return self.items.pop()  
    def empty_stack(self):
        self.items=[]
    def __str__(self) -> str:
        res=""
        for item in self.items:
            res += str(item) +" "
        return res[:-1]
    def peek(self):
        return self.items[-1]
    def empty_stack(self):
        self.items=[]
mystack1= stack()
mystack1.push(1)
mystack1.push(2)
mystack1.push(3)
print(mystack1)
mystack1.pop()
print(mystack1)
print(mystack1.peek())
mystack1.empty_stack()
print(mystack1)