class Array(object):
    def __init__(self,sizeOfArray, arrayType=int) -> None:
        self.sizeOfArray=len(list(map(arrayType, range(sizeOfArray))))
        self.arrayItems = [arrayType(0)]*sizeOfArray
    
    def __str__(self) -> str:
        return str(self.arrayItems)

    def __len__(self):
        return len(self.arrayItems)
    
    def insert(self,keyToInsert, position):
        if self.sizeOfArray >position:
            for i in range(self.sizeOfArray-2, position-1,-1):
                self.arrayItems[i+1]=self.arrayItems[i]
            self.arrayItems[position]=keyToInsert
        else:
            print("Size of array is ", self.sizeOfArray)
    
a= Array(10,int)
for i in range(10):
    a.insert(i,i)

print(a)
a.insert(3,3)
print(a)