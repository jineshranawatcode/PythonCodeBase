def testmethod(self):
    print("this is test class method")
class Base:
    def myfun(self):
        print("This is inherited method")

#create test class dynammically using type() method directly
Test = type('Test', (Base,) , dict(x="jinesh",my_method=testmethod))

print(type(Test))

test_obj =Test()

print(type(test_obj))

test_obj.myfun()

test_obj.my_method()
print(test_obj.x)