class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber =idnumber
    
    def display(self):
        print(self.name)
        print(self.idnumber)
    
    def idnumber(self):
        print("My name is {}".format(self.name))
        print("My idnumber is {}".format(self.idnumber))


class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)  #or to be called after or befor your choice  Person.__init__(self,name,idnumber)
        self.salary =salary
        self.post =post

    def details(self):
        print("My name is {}".format(self.name))
        print("My Idnumber is {}".format(self.idnumber))
        print("My post is {}".format(self.post))
    
a = Employee("rahul",236387,1872638,"Intern")
a.display()
a.details()