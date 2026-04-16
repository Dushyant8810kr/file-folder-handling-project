from pathlib import Path
import os

print("Options : ")
print("1. Create a folder.")
print("2. Read files and folders.")
print("3. Update the folder.")
print("4. Delte te folder.")

option = int(input("Choose an option : "))


def create_folder():
    try:
        name = input("Enter your Folder name : ")                       # taking the name as input from user for creatinga folder
        p = Path(name)                                                  # copy the path of inputed name    
        p.mkdir()                                                       # making the directiory for inputed name path
        print("Folder is successfully created.")                        # simmply prints the message after succesful creation of folder
    except Exception as err:                                            # if there is any issue in folder creation then this will handle this.
        print("Your folder is already exist!!")                         # simply prints taht your file is already exist.

def read_Folder():
    p = Path("")
    count = 1                                                           # for indexing purpose for folder or file
    for item in os.listdir(p) :                                         # os.listdir(p) ->get all files/folders
        if item.startswith("."):                                        #skip hiddenFiles like .git , .vscode  etc
            continue
        print(f"{count}",item)                                          # print the file/folder with count
        count+=1
        


if option==1:
    create_folder()

if option==2:
    read_Folder()



