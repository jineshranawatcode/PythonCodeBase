class Queue:
    def __init__(self) -> None:
        self.items =[]
    
    def enqueue(self,items):
        self.items.append(items)
    
    def is_empty(self):
        if not self.items:
            return True
        return False
    
    def dequeue(self,number_of_items=1):
        counter =0
        while not self.is_empty() and counter< number_of_items:
            self.items.pop(0)
            counter=counter+1
    
    def __str__(self) -> str:
        res ="start - "
        for item in self.items:
            res+= str(item)+" "
        return res +'-end'
    
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
q.dequeue(2)
print(q)
q.dequeue()
print(q)