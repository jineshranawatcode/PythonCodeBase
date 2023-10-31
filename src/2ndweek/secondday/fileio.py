file=open(r"C:\Codebase\PythonCodeBase\src\2ndweek\secondday\Jinesh.txt","r")
print(file.read(5))


with open(r"C:\Codebase\PythonCodeBase\src\2ndweek\secondday\Jinesh.txt") as file:
    data = file.readlines()
    for line in data:
        word =line.split()
        print(word)

file = open(r"C:\Codebase\PythonCodeBase\src\2ndweek\secondday\Jineshc371data.txt","w")
file.write("Jinesh Python class is started\n")
file.write("After which we would have sql classs")
file.close()
#print(data)

import pandas as pd
s1=pd.Series([1, 2 , 3 , 4 ,5])
print(s1)