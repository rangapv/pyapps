import sqlite3
comm = sqlite3.connect ('new.db')
print ("hello")
print ("success in Db")

#comm.execute('''CREATE TABLE T1
#        (ID INT PRIMARY KEY NOT NULL,
#        NAME    TEXT NOT NULL);''')

print ("Table created success")

comm.execute("INSERT INTO T1 (ID,NAME) \
        VALUES (01, 'Ranga')");

print ("Insert in Tabel success")
comm.close()
