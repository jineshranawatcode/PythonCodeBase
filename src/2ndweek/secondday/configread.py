from decouple import config

database_host=config('DATABASE_HOST')
print(database_host)

import os

c = os.getcwd()
print(c)
os.chdir("c:/Codebase/PythonCodeBase/src/2ndweek/secondday/")
c = os.getcwd()
print(c)
directory="c:/Codebase/PythonCodeBase/src/2ndweek/secondday"


import subprocess
with open(r"output.txt","wb") as f:
    subprocess.run(["python","filemode.py"],stdout=f,text=True)