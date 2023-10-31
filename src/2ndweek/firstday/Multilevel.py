class GrandFather:

    def __init__(self,grandfathername) :
        self.grandfathername =grandfathername

class Father(GrandFather):
    def __init__(self, grandfathername,fathername):
        super().__init__(grandfathername)
        self.father =fathername

class Son(Father):
    def __init__(self, grandfathername, fathername, sonname):
        super().__init__(grandfathername, fathername)

        self.sonname = sonname
    
    def print_name(self):
        print(self.grandfathername)
        print(self.father)
        print(self.sonname)

s1=Son("prince","rampal","lal mani")
print(s1.grandfathername)
s1.print_name()