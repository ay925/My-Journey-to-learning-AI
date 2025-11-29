# fileopen=open("01_basics_python/filehandling/demo.txt","r")
# contant=fileopen.read()
# print(contant)


# fileopen.close()
# filewrite=open("01_basics_python/filehandling/file.txt","w")
# filewrite.write(contant)
# filewrite.close()

#with statment
with open("01_basics_python/project/fileproject.py","r") as fileopen:
    contant=fileopen.read()
    print(contant)

with open("01_basics_python/filehandling/file2.txt","w") as filewrite:
    filewrite.write(contant)
    