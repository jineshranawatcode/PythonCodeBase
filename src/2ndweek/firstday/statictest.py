class Myclass:
    def __init__(self,value):
        self.value =value

    @staticmethod
    def get_max_value(x,y):
        return max(x,y)

obj = Myclass(10)

print(Myclass.get_max_value(20,30))

print(obj.get_max_value(20,30))