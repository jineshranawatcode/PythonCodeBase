file = open("test.txt","a+")

file.write("Hellow World!")

file.seek(0)

data = file.read()

print(data)

file.close()