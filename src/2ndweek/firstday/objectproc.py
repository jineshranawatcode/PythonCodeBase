class Dog:
    attr1="mammal"

    def __init__(self, name):
        self.name=name

    def speak(self):
        print("My name is {}".format(self.name))
    
Rodger =Dog("Rodger")
tommy= Dog("tommy")

print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is a {}".format(tommy.__class__.attr1))

print("Name is {}".format(Rodger.name))
print("Name is {}".format(tommy.name))

Rodger.speak()
tommy.speak()