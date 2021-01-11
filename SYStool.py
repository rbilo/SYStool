"""
goals for this program:
- can edit txts
- can combine multiple txts into one txt (done!)
- can txt to db (done 50%!)
- can db to txt
- recognise which task is being performed via the flag in command line (done!)
- can do all this via command line, not using argparse
"""
import sys
import sqlite3
import os
"""
current task:
- Create Database functionality with sqlite (finished)
- create ability to transfer the contents of a txt into a database (finished)
"""

typeList = ['-txt', '-db']     # -txt prepares program to work with txts, vice versa for -db
flagList = ['-c', '-v', '-a'] # -c combines files, -v will validate files, -a adds entries to a db from a txt file,
#'-d', '-n']
# -d duplicates a file
# -n creates a new db from a txt file
def help():
    message = """
Help for SYStool.py:

all commands must be formatted in form: python SYStool.py -fileExtension -actionflag file.fileExtension
example: python SYStool.py -txt -c file.txt file1.txt
supported file extension flags: -txt, -db
supported action flags: -c, -v, -a, 

-c: combines two files together into one, inherits file extension from flag

-v: validates that all provided files are accessible, as long as they have the same file extension as the first flag

-a: adds entries from txts into one pre-existing database

warning: all txts must be formatted in a specific manner, see the README on github.com/rbilo/SYStool
"""
    #commented out functions which are in development -d, -n
"""
-d: creates a copy of a pre-existing file, with fileName "originalFileCopyx.filext". x is an integer which counts up from 0

-n: creates a new database from the contents of a pre-existing txt
"""
    print(message)

def listToString(list):
    str1 = " "
    return(str1.join(list))

def txtWorker(fileList):
    """
    this function serves to ensure all txts provided are operable
    """
    index = 0           # variable which iterates through all availible files
    badFileNo = 0     #keeps track of the amount of bad/unaccessible files

    for i in range(len(fileList)):
        """
        loop iterates through the files provided, opens each to check if they are accessible
        if accessible, does nothing, pretty sure closes files when done via with open
        if inaccessible, you can guess :()
        """
        file = fileList[index]
        try:
            with open(file) as f:
                print("File:", file, "available")
                index += 1

        except IOError:
            print("File:", file, "not available.")
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

def combine(fileList):

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
    print("finished")

def addTo(fileList):

    dbFile = fileList[2]
    if len(dbFile) == 1:
        fileName = dbFile[0] #ensures there is only one target database, selects this database as the file to be edited
        # this db has already been verified to exist earlier, so no error can occour here I hope

        conn = sqlite3.connect(fileName)
        print("opened target database successfully")
        cursor = conn.cursor()

        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [
        v[0] for v in cursor.fetchall()
        if v[0] != "sqlite_sequence"
        ]
        # can only add to one table at a time, therefore detects all tables, adds to list called tables

        if len(tables) == 1:
            table = listToString(tables)
        elif len(tables) == None:
            print("No tables in target database! there must be at least 1 table.")
        else:
            tableCount = 1
            tableDex = 0
            print("multiple tables detected!")
            # in the case of multiple tables, prints all tables and assigns them a number.
            for i in range(len(tables)):
                print(tableCount, ":", tables[tableDex])
                tableCount += 1
                tableDex += 1
            # goes on to ask user to choose which table they want to use. I use nested loops for input validation
            while True:
                try:
                    tabledex = str(tableDex)
                    message = "which table would you like to use? 1 to " + tableDex
                    choice = int(input(message))
                    #for some reason, the best way to create a message with a variable number in it is to convert to string, then concatenate into a var, then call the var
                except ValueError:
                    print("integer responses only!")
                if choice > (tablecount - 1) or choice < 1:
                    print("answer out of range!")
                else:
                    break

            table = tables[choice - 1]

            tableTemp = listToString(table)
            table = tableTemp.replace(" ", "")

        txtCount = 0
        for i in range(len(fileList[3])): #iterates through all txt files
            file = open(fileList[3][txtCount], 'r')
            txtCount += 1

            cursor = conn.execute('select * from ' + table)
            names = list(map(lambda x: x[0], cursor.description)) #creates list of all named columns in our target table
            ID = names[0] #gets the name of the ID column we use in the target database

            cursorCOM = ("SELECT MAX(" + ID +") FROM " + table +";") #creates SQL command to get the largest ID in the db, this value is used to prevent duplicate ID's
            cursor.execute(cursorCOM) #executes pre-written SQL command
            minID = cursor.fetchall() #minID (minimumID) = largest ID in table
            minID = minID[0] #because of how fetchall works, and how data is stored, miniID is an integer inside a tuple inside a list. we are getting just the int
            minID1 = int(''.join(map(str, minID))) #got the int!
            minID = minID1 + 1 #cannot have duplicate IDs, therefore +1 for next unique ID

            names = listToString(names)
            names = names.replace(" ", ",")

            for line in file:
                minString = str(minID) #in order to concatenate an SQL command, we need all involved vars to be strings
                line = line.rstrip('\n') #removing any stray \n's left in the string
                executeMSG = "INSERT INTO " + table + " (" + names + ") \
VALUES (" + minString + ", " + line +")"
                minID += 1
                conn.execute(executeMSG); #executes the SQL command we just made
                conn.commit()

            file.close()

        print("operation complete!")

        conn.close()

    else:
        print("There can only be one target database!")

def dbOperation(fileList, command):

    if command == "-a":
        if fileList[0] < 1:
            addTo(fileList)

        else:
            print("database error!")

def txtOperation(fileList, command):
    """
    in this function, all operations related to editing txt files will go down
    """

    if command == "-c":
        combine(fileList)

    else:
        print("finished!")

def dbSplit(fileList):
    """
    """

def dbTypeVerify(fileList):
    """
    function in which the db type verification happens
    """
    dbList = []
    counter = 0
    length = 0
    length = len(fileList)
    for i in range(length):
    # first seperates the .db files from the fileList
        temp = fileList[counter]
        if ".db" in temp:
            dbList.append(temp)
            del fileList[counter]
        else:
            counter += 1

    #at this point we should have fileList containing txts only, and dbList containing dbs only
    counter = 0
    notAvailable = 0
    length = len(dbList)
    faulty = 0

    if length > 0:
        for i in range(length):

            dbName = dbList[counter]
            dbYes = os.path.exists(dbName)
            counter += 1
            if dbYes:
                print("database:", dbName, "available")
            else:
                print("database:", dbName, "not available.")
                notAvailable += 1

    elif length == 0:
        print("no databases")

    if len(fileList) > 0:
        faulty = txtWorker(fileList)

    returnList = []
    returnList.append(faulty)
    returnList.append(notAvailable)
    returnList.append(dbList)
    returnList.append(fileList)

    return(returnList)

#this huge if tree is the reason you use argparse when parsing command line arguments
#yes this is a huge mess, but it works the time being :|

"""
TODO for this part of the code:

some form of logic tree which utilises parent and children system for progressing through parsing the arguments
staring at all these if statements hurts my soul
"""
fileList = []
if sys.argv[1] != "-h":
    if len(sys.argv) > 3: #ensures arguments for filetype, operation, and at least one file is provided
        if sys.argv[1] in typeList:
            fileType = sys.argv[1]
            fileList = sys.argv[3:]     #creates new list of filenames only
            if sys.argv[2] in flagList:
                dbList = dbTypeVerify(fileList)
                faulty = dbList[0] + dbList[1]
                if faulty == 0:
                    if sys.argv[1] == typeList[0]:
                        txtOperation(fileList, sys.argv[2])
                    elif sys.argv[1] == typeList[1]:
                        dbOperation(dbList, sys.argv[2])


                    else:
                        print("you aren't supposed to be able to trigger this message :?")
                else:
                    print("specified files unavailable at start of operation. please check if desired files are present and restart program")
            else:
                print("No function arguments provided!")
        else:
            print("No filetype arguments provided!")

    else:
        print("Invalid input. must be in form: python SYStool.py (file flag) (action flag) (files)")
else:
    help()
