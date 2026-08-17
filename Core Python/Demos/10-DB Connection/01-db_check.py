import mysql.connector
con = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'rutuja',
    database = 'student'
)
if con.is_connected:
    print("Done")
cur = con.cursor()
q = "select * from student"
cur.execute(q)
# row=cur.fetchall()
# row = cur.fetchone()
row = cur.fetchmany(3)
print(row)