import mysql.connector
conn=mysql.connector.connect(user='root', password='{Hallelujah};0657', host='127.0.0.1', database='database1')
sql_select_query="SELECT *FROM database1.tab"
cursor= conn.cursor()
cursor.execute(sql_select_query)
records=cursor.fetchall()
print("Total number of rows :", cursor.rowcount)
print("RECORD:")
for row in records:
    print("ID =",row[0])
    print("First Name= ", row[1])
    print("Last  Name=", row[2])
    print("City=", row[3])
    print("State=", row[4])
    print("Pincode=", row[5])
cursor.execute("UPDATE database1.tab SET City='Geneva' WHERE ID='2'")
conn.commit()