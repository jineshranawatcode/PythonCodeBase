class Bird:
    def intro(self):
        print("There are many types of bird")
    
    def flight(self):
        print("Most of the bird can fly but some cannot")


class sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")
    

class ostrich(Bird):
    def flight(self):
        print("Ostrich cannot fly")

obj_bird=Bird()
obj_Sparrow=sparrow()
obj_ostrich=ostrich()

obj_bird.intro()
obj_bird.flight()

obj_Sparrow.intro()
obj_Sparrow.flight()

obj_ostrich.intro()
obj_ostrich.flight()