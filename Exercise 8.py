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
from geopy import distance

airportName = ["", ""]
airportPos = [[0, 0], [0, 0]]

for i in range(2):
    airportCode = input(f"Input ICAO code of airport {i + 1}: ")

    sql = "select name, latitude_deg, longitude_deg from airport "
    sql += "where ident = '" + airportCode + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    airportName[i] = result[0][0]
    airportPos[i][0] = result[0][1]
    airportPos[i][1] = result[0][2]

    #print latitude and longitude of airport
    #print(airportPos[i][0])
    #print(airportPos[i][1])


print(f"Distance between {airportName[0]} and {airportName[1]} is ", end = '')
print(f"{distance.distance(airportPos[0], airportPos[1]).km:.3f} km")
