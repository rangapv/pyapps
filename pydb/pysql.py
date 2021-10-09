import sqlite3
comm = sqlite3.connect ('new.db')
print ("hello")
print ("success in Db")

comm.execute('''CREATE TABLE T1
        (ID INT PRIMARY KEY NOT NULL,
        NAME    TEXT NOT NULL);''')

comm.close()
