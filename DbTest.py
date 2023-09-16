import mysql.connector

cnx = mysql.connector.connect(
    host='****',
    user='****',
    password='****',
    database='****',
    port = '****'
)

cursor = cnx.cursor()

'''
query = "INSERT INTO mytbl (FirstName, LastName) VALUES (%s, %s)"
values = ("s", "p")
cursor.execute(query, values)
cnx.commit()
'''

query = "SELECT * FROM mytbl"
cursor.execute(query)
# Fetch all the rows
rows = cursor.fetchall()
for row in rows:
    print(row)


# Close the cursor and connection
cursor.close()
cnx.close()
