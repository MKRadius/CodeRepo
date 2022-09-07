"""
#Exercise 6.1
import random
diceNum = 0

def rollDice():
    diceNumber = random.randint(1, 6)
    return diceNumber

print("Time to roll a dice")
while diceNum != 6:
    diceNum = rollDice()
    print("You got", diceNum)



#Exercise 6.2
import random
diceNum = 0

def rollDice(sides):
    diceNumber = random.randint(1, sides)
    return diceNumber

diceSides = int(input("How many sides does the dice have: "))
maxDiceNum = int(input("Which number do you want to get: "))
print("Time to roll the dice")

while diceNum != maxDiceNum:
    diceNum = rollDice(diceSides)
    print("You got", diceNum)



#Exercise 6.3
def gallonsToLiters(galllons):
    print(gallons, "US gallons =", gallons * 3.785, "liters")

while True:
    print("Input negative number to exit")
    gallons = float(input("Input gallons: "))

    if gallons < 0:
        print("Exiting...")
        break

    gallonsToLiters(gallons)



#Exercise 6.4 
numberList = []

def sumOfNumberInList(numList):
    numSum = 0
    for i in numList:
        numSum += i
    return numSum

while True:
    userInput = input("Input: ")
    
    if userInput == '':
        break
    
    userNumber = int(userInput)
    numberList.append(userNumber)

print("Sum of all the numbers in the list:", sumOfNumberInList(numberList))




#Exercise 6.5
originalList = []
newList = []

def removeUnevenNumber(numList):
    for i in reversed(numList):
        if i % 2 == 1:
            numList.remove(i)        
    return numList

while True:
    userInput = input("Input: ")
    
    if userInput == '':
        break
    
    userNumber = int(userInput)
    originalList.append(userNumber)

newList = list(originalList)
removeUnevenNumber(newList)

print("Original list:", originalList)
print("New list:     ", newList)
"""


#Exercise 6.6