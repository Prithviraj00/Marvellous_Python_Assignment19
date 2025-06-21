import os
import sys
import time

def DirectoryWatcher(DirectoryName,Extension):
    
    flag = os.path.isabs(DirectoryName)
    
    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)
        
    flag = os.path.exists(DirectoryName)
    
    if (flag == False):
        print("The path is invalid")
        exit()
    
    flag = os.path.isdir(DirectoryName)
    if (flag == False):
        print("Path is vaild but the target is not a directory")
        exit()
        
      
    for FolderName, SubFolderNames, FilesNames in os.walk(DirectoryName):
           for fname in FilesNames :
               if(fname.endswith(Extension)):
                    print("File Name :",fname)
                
def main():
    Broder = "-"*60
    print(Broder)
    print("----------------Marvellous Automation---------------------")
    print(Broder)
    
    if(len(sys.argv) == 2):
        if((sys.argv[1]=="--h") or(sys.argv[1]=="--H")):
            print("This application is used to perform display all files with that extension")
            print("Display all files Extension in directory Automation script")
        
        elif((sys.argv[1]=="--u") or(sys.argv[1]=="--U")):
            print("Use the given script as")
            print("ScriptName.py NameOfDirectory  file extension")
            print("Please provide valid absolute path")
            
    elif(len(sys.argv)==3):
            DirectoryWatcher (sys.argv[1],sys.argv[2])
            
    else :
        print("Invalid number of command line argument")
        print("Use the gievn flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")
    print(Broder)
    print("----------------Thank you using our script----------------")
    print("-----------------Marvellous Infosystems-------------------")
    print(Broder)

if __name__ =="__main__":
    main()