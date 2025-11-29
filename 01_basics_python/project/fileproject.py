import os
file=input("Enter the file location :")
if os.path.exists(file):
    print("This file is alraidy exist !!")
else:
    print("File dose not exist")
    asking_create_file=input("Are you create file {y/n} : ")
    if(asking_create_file.lower()=="y"):
        with open(file,"w") as filecreated:
            print("file created scussecfully same location.")
    else:
        print("Ok no warry")
