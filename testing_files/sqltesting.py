import sqlite3

def listToString(list):
    str1 = " "
    return (str1.join(list))

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

conn =  sqlite3.connect("test.db")
print("opened database successfully")

cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [
    v[0] for v in cursor.fetchall()
    if v[0] != "sqlite_sequence"
    ]

if len(tables) < 2:
    tables = listToString(tables)
else:
    tablecount = 1
    tabledex = 0
    print("More than one table detected!")
    for i in range(len(tables)):
        print(tablecount, ":", tables[tabledex])
        tablecount += 1
        tabledex += 1
    while True:
        try:
            tabledex = str(tabledex)
            mensage = ("which table should data be entered to? 1 to " + tabledex)
            choice = int(input(mensage))
        except ValueError:
            print("integers response only!")
        if choice > (tablecount - 1) or choice < 1:
            print("answer not in range!")
        else:
            break

    choice -= 1
    tables = tables[choice]

tableTemp = listToString(tables)
tables = tableTemp.replace(" ", "")
    
file = open('values.txt', 'r')

cursor = conn.execute('select * from '+tables)
names = list(map(lambda x: x[0], cursor.description))

"""
names = [description[0] for description in cursor.description]
"""


ID = names[0]

cursorCOM= ("SELECT MAX(" +ID+ ") FROM " +tables+ ";")
cursor.execute(cursorCOM)
minID = cursor.fetchall()
minID = minID[0]
res = int(''.join(map(str, minID)))
minID = res + 1

names = listToString(names)
names = names.replace(" ", ",")

for line in file:
    minString = str(minID)
    line = line.rstrip('\n')
    executeMessage = "INSERT INTO " + tables + " (" + names + ") \
VALUES ("+ minString +", " + line + ")"
    minID += 1
    conn.execute(executeMessage);
    conn.commit()
    
print("operation complete!");

conn.close()
