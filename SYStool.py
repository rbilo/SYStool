"""
goals for this program:
- can edit txts
- can combine multiple txts into one txt (done!)
- can txt to sql
- can sql to txt
- recognise which task is being performed via the flag in command line (done!)
- can do all this via command line, not using argparse
"""
import sys
"""
current task:
"""

typeList = ['-txt']     # -txt prepares program to work with txts, vice versa for -sql
flagList = ['-c', '-v']     # -c combines files, -v will validate files

def txtWorker(fileList):
    """
    this function serves to ensure all files provided are operable
    """
    index = 0           #iterates through all availible files
    badFileFlag = 0     #keeps track of the amount of bad/unaccessible files
    faulty = []         #list for the faulty files
    print("ensuring files are operable...")

    for i in range(len(fileList)):
        """
        loop iterates through the files provided, opens each to check if they are accessible
        if accessible, does nothing, pretty sure closes files when done via with open
        if inaccessible, you can guess :()
        """
        file = fileList[index]
        try:
            with open(file) as f:
                print("File:", file, "accessible")
                index += 1

        except IOError:
            print("File:", file, "not accessible. Ensure filenames are correct and/or file is in directory")
            badFileFlag += 1
            faulty.append(file)
            index += 1;


    tempFaulty = faulty
    faulty.clear()
    faulty.append(badFileFlag)
    faulty.append(tempFaulty)

    return(faulty)

def txtOperation(fileList, command):
    """
    in this function, all operations related to editing the provided files will go down
    """

    if command == "-c":

        fileEnd = 0
        while True:
            """
            ensures that the new file always has a unique filename, so as to not overwrite any pre-existing files
            """
            fileEnd1 = str(fileEnd)
            fileName = ("combinded" + fileEnd1 + ".txt")
            try:
                with open(fileName) as f:
                    fileEnd += 1
            except IOError:
                break

        newFile = open(fileName, "a+")

        index = 0

        for i in range(len(fileList)):
            with open(fileList[index], "r") as file:
                temp = file.read().rstrip('\n')
                newFile.write(temp)
                index += 1
                file.close()

        print("files combined! filename:", fileName)
        newFile.close()
        printChoice = input("would you like to see the file contents? (y/n) ")
        if printChoice == "y":
            with open(fileName, "r") as file:
                temp = file.read().rstrip('\n')
                print(temp)

        print("Finished!")

    else:
        print("finished!")


def txtGO(faulty, fileList):

    if faulty[0] == 0:
        print("no files faulty or unavailible.")

    else:
        num = faulty[0]
        print("you have:", num,"faulty file(s). please check these and restart program")

fileList = []
if len(sys.argv) > 3: #ensures arguments for filetype, operation, and at least one file is provided

    if sys.argv[1] in typeList:
        fileType = sys.argv[1]
        fileList = sys.argv[3:]     #creates new list of filenames only
        if sys.argv[2] in flagList:
            faulty = txtWorker(fileList)         #runs functio nwhich validates the files (runs by default independent of flags
            txtGO(faulty, fileList)
            txtOperation(fileList, sys.argv[2])
        else:
            print("No function arguments provided!")
    else:
        print("No filetype arguments provided!")

else:
    print("Invalid input. must be in form: python SYScat.py (file flag) (action flag) (files)")
