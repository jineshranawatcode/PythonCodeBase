import os

def create_file(filename):
    try:
        with open(filename,"w") as f:
            f.write("Hello world]n")
        print("File "+filename +"created sucessfully")
    except IOError:
        print("Error could not crete file"+filename)

def read_file(filename):
    try:
         with open(filename,"r") as f:
             contents = f.read()
             print(contents)
    except IOError:
        print("Could not read file"+filename)

def append_file(filename,text):
    try:
        with open(filename,"a") as f:
            f.write(text)
        print("text appended to file "+filename+"with content "+ text +" sucssufully")
    except IOError:
        print("Error could not append to file "+ filename)

def rename_file(filename,new_filename):
    try:
        os.rename(filename,new_filename)
        print("File "+filename +" reenamed to "+ new_filename +" succssessfully")
    except IOError:
        print("Could not rename file "+ filename)
# r, w , a , r+  open the file read and write , w+  open the file write ad read  , a+ open fule reading and writing , data inserted at end , 
# rb:- binaray , rb+  :- open and read and write in bonary format  , wb :- open the file content binary format , wb+ open the file write in binary and read from biary
#, ab, ab+
def deletefile(filename):
    try:
        os.remove(filename)
        print("File "+filename+"deeleeted scuessfully")
    except IOError:
        print("Error could not delete file"+filename)

if __name__ =="__main__":
    filename="example.txt"
    new_filename="new_Example.txt"
    create_file(filename)
    read_file(filename)
    append_file(filename,"This is some additional text \n")
    read_file(filename)
    rename_file(filename,new_filename)
    read_file(new_filename)
    deletefile(new_filename)