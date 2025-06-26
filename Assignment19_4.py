import os
import sys
import time


def DirectoryWatcher(DirectoryName, Directoryname1, Extension):

    flag = os.path.isabs(DirectoryName)

    if flag == False:
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if flag == False:
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)
    if flag == False:
        print("Path is vaild but the target is not a directory")
        exit()

    flag = os.path.isabs(Directoryname1)
    if flag == False:
        Directoryname1 = os.path.abspath(Directoryname1)
    flag = os.path.exists(Directoryname1)

    flag = os.path.exists(Directoryname1)
    flag = os.mkdir(Directoryname1)

    for FolderName, SubFolderNames, FilesNames in os.walk(DirectoryName):
        for fname in FilesNames:
            if fname.endswith(Extension):
                file_path = os.path.join(FolderName, fname)
                file_path2 = os.path.join(Directoryname1, fname)

                obj1 = open(file_path, "rb")
                data = obj1.read()

                obj2 = open(file_path2, "wb")
                obj2.write(data)

                print("File name :", fname)


def main():
    Broder = "-" * 60
    print(Broder)
    print("----------------Marvellous Automation---------------------")
    print(Broder)

    if len(sys.argv) == 2:
        if (sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
            print("This script copies files with specific extension from one directory to another.")


        elif (sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
            print("Use the given script as")
            print("DirectoryCopy.py <1st Directory> <2nd Directory> <extension>")
            print("Please provide valid absolute path")

    elif len(sys.argv) == 4:
        DirectoryWatcher(sys.argv[1], sys.argv[2], sys.argv[3])

    else:
        print("Invalid number of command line argument")
        print("Use the gievn flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")
    print(Broder)
    print("----------------Thank you using our script----------------")
    print("-----------------Marvellous Infosystems-------------------")
    print(Broder)


if __name__ == "__main__":
    main()
