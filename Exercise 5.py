#Exercise 5.1
import random

dice = int(input("Input number of dices: "))
dice_sum = 0

for i in range(dice):
    dice_num = random.randint(1, 6)
    dice_sum += dice_num

print("Sum of dice:", dice_sum)



#Exercise 5.2
userInput = "input"
number = []

while True:
    userInput = input("Input: ")
    
    if userInput == '':
        break
    
    userNumber = int(userInput)
    number.append(userNumber)

if len(number) != 0:
    number.sort(reverse = True)
    print("5 biggest numbers in descending order:")
    
    if len(number) >= 5:
        for i in range(5):
            print(number[i], " ", end = '')
        print("")
    
    else:
        for i in range(len(number)):
            print(number[i], " ", end = '')
        print("")

else:
    print("No input.")
  


#Exercise 5.3
import math
inputNumber = int(input("Input number: "))
primeStatus = True

if inputNumber == 0 or inputNumber == 1:
    print(inputNumber, "is not a prime number")
else: 
    for i in range(2, int(math.sqrt(inputNumber)) + 1):
        if inputNumber % i == 0:
            primeStatus = False
            break

    if primeStatus is False:
        print(inputNumber, "is not a prime number")
    else:
        print(inputNumber, "is a prime number")
        


#Exercise 5.4
citiesName = []
print("Input 5 cities name")

for i in range(5):
    userInput = input(f"Input city {i + 1} name: ")
    citiesName.append(userInput)

for i in citiesName:
    print(f"City {citiesName.index(i) + 1} name is: {i}")
