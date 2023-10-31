class recursiveFunction:
    def __init__(self,n):
        self.n=n
        print(n)
    
    def run(self,n=None):
        if n is None:
            n= self.n
        if n<=0:
            return
        print("Running recursive with n= ",n)
        self.run(n-1)
    
    def __del__(self):
        print("recursive destryed")
    
obj = recursiveFunction(5)
obj.run()

del obj