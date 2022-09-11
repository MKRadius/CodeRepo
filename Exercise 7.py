"""
#Exercise 7.1
seasonOfTheYear = ("Spring", "Summer", "Autumn", "Winter")

userMonth = int(input("Input month (1 - 12): "))
userSeason = seasonOfTheYear[userMonth // 3 - 1]

print(f"Month {userMonth} is {userSeason}")
"""

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
    