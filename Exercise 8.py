import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)


#Exercise 8.1
inputICAO = input("Input ICAO: ")

sql = "select name, municipality from airport "
sql += "where ident = '" + inputICAO +"'"

#print(sql)

cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()

if cursor.rowcount > 0:
    for row in result:
        print(f"Airport: {row[0]}\nLocation: {row[1]}")



#Exercise 8.2
userInput = input("Area code: ")

sql = "select name, type from airport "
sql += "where iso_country = '" + userInput + "' order by type"

cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()

if cursor.rowcount > 0:
    for row in result:
        print(f"Airport: {row[0]}")
        print(f"Type: {row[1]}\n")



#Exercise 8.3

