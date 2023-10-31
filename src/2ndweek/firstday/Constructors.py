class Myclass:
    def __init__(self,name=None) -> None:
        if name is None:
            print("Empty/Defauly Constructor called")
        else:
            self.name=name
            print("parametrized with value",self.name)
    
    def method(self):
        if hasattr(self,'name'):
            print("Method called with name ",self.name)
        else:
            print("method without name")
    
obj1=Myclass()

obj1.method()

obj2=Myclass("John")
obj2.method()
