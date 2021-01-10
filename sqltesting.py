import sqlite3

def listToString(list):
    str1 = " "
    return (str1.join(list))

conn =  sqlite3.connect("test.db")
print("opened database successfully")

cursor = conn.cursor()
cursor.execute("SELECT * FROM COMPANY")
results = cursor.fetchall()
minID = (len(results))
minID += 1

cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [
    v[0] for v in cursor.fetchall()
    if v[0] != "sqlite_sequence"
    ]
print(tables)

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
    
file = open('values.txt', 'r')
count = 0

cursor = conn.execute('select * from COMPANY')
"""
names = list(map(lambda x: x[0], cursor.description))
print(names)
"""
names = [description[0] for description in cursor.description]


names = listToString(names)
names = names.replace(" ", ",")

for line in file:
    count += 1
    line = line.rstrip('\n')
    minID1 = str(minID)
    executeMessage = "INSERT INTO " + tables + " (" + names + ") \
VALUES ("+ minID1 + "," + line + ")"
    minID += 1
    conn.execute(executeMessage);
    conn.commit()
    


cursor = conn.execute("SELECT ID,NAME,ADDRESS,SALARY from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3])


print("operation complete!");
conn.close()
