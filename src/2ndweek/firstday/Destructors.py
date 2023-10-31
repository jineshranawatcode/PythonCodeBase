class Employee:
    def __init__(self):
        print("Employee Created")
    
    def __del__(self):
        print("Destructor called")
    
def create_obj():
    obj=Employee()
    return obj

obj= create_obj()
#del obj
print("Prgram end")