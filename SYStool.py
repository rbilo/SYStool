"""
goals for this program:
- can edit txts
- can combine multiple txts into one txt (done!)
- can txt to db
- can db to txt
- recognise which task is being performed via the flag in command line (done!)
- db to spreadsheet
- txt to spreadsheet
- can do all this via command line, not using argparse
"""
import sys
"""
current task:
txt to db. (adding contents of a txt to a pre-existing db has already been done in testing environment, implimenting into the tool itself currently)
db to txt
edit txts
"""

typeList = ['-txt']     # -txt prepares program to work with txts, -db for databases
flagList = ['-c', '-v']     # -c combines files, -v will validate files

def help():
    message = """
Help for SYStool.py:

all commands must be formatted in form: python SYStool.py -fileExtension -actionflag file.fileExtension
example: python SYStool.py -txt -c file.txt file1.txt
supported file extension flags: -txt
supported action flags: -c, -v

-c: combines two files together into one, inherits file extension from flag

-v: validates that all provided files are accessible, as long as they have the same file extension as the first flag
"""
    print(message)

def txtWorker(fileList):
    """
    this function serves to ensure all files provided are operable
    """
    index = 0           #iteratable variable to loop through all availible files
    badFileNo = 0     #keeps track of the amount of bad/unaccessible files
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
            badFileNo += 1
            index += 1;

    return(badFileNo)

def fileNameGen(name, end):

    fileEnd = 0
    while True:
        fileEnd1 = str(fileEnd)
        fileName = (name + fileEnd1 + end)
        try:
            with open(fileName) as f:
                fileEnd += 1
        except IOError:
            break

    return(fileName)

def txtOperation(fileList, command):
    """
    in this function, all operations related to editing the provided files will go down
    """

    if command == "-c":

        fileName = ""
        fileName = fileNameGen("combined", ".txt")

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

        print("Finished!")

    else:
        print("finished!")

def txtGO(faulty, fileList):

    if faulty == 0:
        print("no files faulty or unavailible.")

    else:
        print("you have:", faulty,"faulty file(s). please check these and restart program")

fileList = []
if sys.argv[1] != "-h":
    if len(sys.argv) > 3: #ensures arguments for filetype, operation, and at least one file is provided

        if sys.argv[1] in typeList:
            fileType = sys.argv[1]
            fileList = sys.argv[3:]     #creates new list of filenames only
            if sys.argv[2] in flagList:
                faulty = txtWorker(fileList)         #runs function which validates the files (runs by default independent of flags
                txtGO(faulty, fileList)
                txtOperation(fileList, sys.argv[2])
            else:
                print("No function arguments provided!")
        else:
            print("No filetype arguments provided!")

    else:
        print("Invalid input. must be in form: python SYScat.py (file flag) (action flag) (files)")
else:
    help()
