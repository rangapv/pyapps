import sqlite3

comm = sqlite3.connect('new.db')

cursor = comm.execute("SELECT id, name from T1")

for row in cursor:
    print ("ID=", row[0])
    print ("Name is", row[1])

comm.close()
