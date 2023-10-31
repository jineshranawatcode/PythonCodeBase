class School:
    def func1(self):
        print("this function is school")
    
class School1(School):
    def func2(self):
        print("function school1")

class Student2(School):
    def func3(self):
        print("function school2")


class Student3(School1,Student2):
    def func4(self):
        print("function school3")

obj =Student3()
obj.func1()
obj.func2()

