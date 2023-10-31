class test:
    def __init__(self,a,b):
        self.a=a
        self.b =b
    
    def __repr__(self):
        return "test a:%s b :%s" %(self.a,self.b)
    
    def __str__(self) -> str:
        return "from str menthod of test a is %s, bi is %s" % (self.a,self.b)

t =test(1234,5678)
print(t)
print([t])