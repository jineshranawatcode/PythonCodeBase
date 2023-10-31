class Base:
    def __init__(self,par1,par2) :
        self.a=par1
        self.__c=par2

class Derived(Base):
    def __init__(self):
        super().__init__("akhsdajs","aasdhgasjhgd")
        print("Calling private member of base class")
        #print(self.__c)

obj1 =Base("uiejide","qdekjhdekjhd")
print(obj1.a)


obj2=Derived()