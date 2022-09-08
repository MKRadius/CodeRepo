"""
name = []

name = input("Your name: ")
index = 0

for i in name:
    print(i)

print("")

while name != "" and index < len(name):
    print(name[index])
    index += 1
"""

inp = 1

while inp > 0:
    result = 1

    inp = int(input("Please type in a number: "))

    if inp <= 0:
        print("Thanks and bye")
        break
    else: 
        for i in range(1, inp + 1):
            #print(i)
            result *= i

        print("The factorial of the number", inp, "is", result)

