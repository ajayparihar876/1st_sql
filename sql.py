import sqlite3
filename =  input("please enter the Database name  ")
table_name =  input("please enter the table name  ")
student_name =  input("please enter the name  ")
contact =  input("please enter the contect no.  ")

#Always open the file
filename = filename+".sqlite3"
fileOpen = open(filename,"a")
# open the database connection
conn = sqlite3.connect(filename)

cur = conn.cursor()
# know  we create the table
cur.execute('CREATE TABLE '+table_name+' (name text, contact text)')
cur.execute("INSERT INTO "+table_name+" (name, contact) VALUES ('"+student_name+"', '"+contact+"')")
#insert data

itrableobj = cur.execute('SELECT * FROM '+table_name)
for row in itrableobj:
    print(row)
    conn.commit()
# close database
conn.close()
#file close
fileOpen.close()

