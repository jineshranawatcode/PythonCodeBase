with open("example.txt","wb") as file:
    data = b'This is a binary \n file'
    file.write(data)

with open("example.txt", "wb+") as file:
    data = b"this is binary \n  file 2d times"
    file.write(data)

    file.seek(0)
    content = file.read()
    print("Write and read content ", content)