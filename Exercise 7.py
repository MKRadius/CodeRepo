#Exercise 7.1
seasonOfTheYear = ("Spring", "Summer", "Autumn", "Winter")

userMonth = int(input("Input month (1 - 12): "))
if 1 <= userMonth <= 12:
    userSeason = seasonOfTheYear[userMonth // 3 - 1]
    print(f"Month {userMonth} is {userSeason}")
else:
    print("Invalid month input")



#Exercise 7.2
name = set()

while True:
    userInput = input("Input name: ")
    
    if userInput == '':
        break

    if userInput in name:
        print("Existing name")
    else:
        name.add(userInput)
        print("New name")

print("Name list:")

for i in name:
    print(i)
  


#Exercise 7.3
airport = dict()

def enterNewAirport(airport):
    inputICAO = str(input("Insert airport ICAO code: "))
    inputName = str(input("Insert airport name: "))

    airport[inputICAO] = inputName
    print("Airport successfully added!\n")
    
    return airport

def fetchExistingAirport(airport):
    inputICAO = str(input("Insert airport ICAO code : "))
    
    if inputICAO in airport:
        print(f"Airport name: {airport[inputICAO]}\n")
    else:
        print("Airport not found.\n")
    
    return airport

while True:
    print("(1) Enter new airport")
    print("(2) Fetch existing airport's information")
    print("(3) Quit")

    userInput = input("Choose your option (1/2/3): ")
    print("")

    if userInput == "1":
        enterNewAirport(airport)
    elif userInput == "2":
        fetchExistingAirport(airport)
    elif userInput == "3":
        print("Exiting...")
        break
    else:
        print("Invalid input. Please try again.\n")
        continue

#Dictionary check
#print(airport)