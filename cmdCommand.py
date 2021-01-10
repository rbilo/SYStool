commandsList = ["python"]

programName = input("what is the name of the python program? full file name, e.g. xyz.py ")
commandsList.append(programName)

any0 = input("any flags? (y/n) ")
if any0 == "y":
    while True:
        flagsName = input("enter the flag designation: ")
        commandsList.append(flagsName)
        anyHeHe = input("any more flags? (y/n) ")
        if anyHeHe != "y":
            break

any1 = input("any suplimentary files? (y/n) ")
if any1 == "y":
    while True:
        text = ("full file name and extension of file ")
        fileName = input(text)
        commandsList.append(fileName)
        any2 = input("any more supplimentary files? (y/n) ")
        if any2 != "y":
            break

str1 = " "
final = str1.join(commandsList)
print(final)
