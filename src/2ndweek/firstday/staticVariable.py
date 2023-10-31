class CSStudent:
    stream ="cse"
    def __init__(self,name,roll):
        self.name =name
        self.roll =roll

a = CSStudent("geek",1)
b=CSStudent("nerd",2)
print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)


print(CSStudent.stream)
a.stream="CSE"
print(a.stream)
print(b.stream)

CSStudent.stream="mech"
print(a.stream)
print(b.stream)