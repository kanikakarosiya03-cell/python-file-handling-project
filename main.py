from pathlib import Path
import os

def creatfile():
    try:
        name = input("Pleae tell file name you want to creat \n :- ")
        path = Path(name)
        if not path.exists():
            with open(name,"w") as fs:
                data = input("Please enter data you want to write \n :- ")
                fs.write(data)
                print("File created succssefully")
        else:
            print("File allready exists give another name  :- ")

    except Exception as err:
        print(f"An error occoured {err}")

def readfile():
    try:
        name = input("Pleae tell file name you want to read :- ")
        path = Path(name)
        if path.exists():
            with open(name,"r") as fs:
                content = fs.read()
                print("Your file content is \n ",content)
            print("File Successfully read ")
        else:
            print("No such file exists ")

    except Exception as err:
        print(f"An error occured {err}")

    
def updatefile():
    try:
        name = input("Pleae tell file name you want to read :- ")
        path = Path(name)
        if path.exists():
            print("Operations")
            print("1 . Rename the file ")
            print("2 . Append the content ")
            print("3 . Overwrite the file")

            choice = int(input("Please enter your choice :- "))
            if choice == 1:
                new_name = input("Please tell your new file name :- ")
                new_path = Path(new_name)

                if not new_path.exists():
                    path.rename(new_path)
                    print("renamed successfully")
                else:
                    print("A file with that name already exists")

            elif choice == 2:
                name = input("Pleae tell file name you want to append :- ")
                path = Path(name)

                if path.exists():
                    with open(name,"a") as fs:
                        data = input("Enter data you want to append : \n")
                        fs.write(" " + data)
                else:
                    print("File not exists")

            elif choice == 3:
                name = input("Pleae tell file name you want to overwrite :- ")
                path = Path(name)

                if path.exists():
                    with open(name,"w") as fs:
                        data = input("Enter data you want to over write : \n ")
                        fs.write(data)
                else:
                    print("File not exists")

    except Exception as err:
        print(f"An error occured {err}")




def deletfile():
    try:
        name = input("Please tell your file name :- ")
        path = Path(name)

        if path.exists():
            path.unlink()
            print("File deleted ssuccessfully ")
        else:
            print("Error no such file exists ")
    except Exception as err:
        print(f"An error occured {err}")


print("Enter 1 to creating a file ")
print("Enter 2 to reading a file  ")
print("Enter 3 to updateing a file ")
print("Enter 4 to deleting a file ")

operations = int(input("Which operation you want to perform :- "))

if operations == 1:
    creatfile()

if operations == 2:
    readfile()

if operations == 3:
    updatefile()

if operations == 4:
    deletfile()


