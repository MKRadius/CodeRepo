# Exercise 4.1
x = 1
while 1 <= x <= 1000:
    if x % 3 == 0:
        print(x)
    x += 1

# Exercise 4.2
conv = float(input("Input inches: "))
while conv >= 0:
    if conv >= 0:
        print(conv, "inches = ", conv * 2.54, "centimeters\n")
        print("Input negative number to exit")
        conv = float(input("Input inches: "))
        if conv < 0:
            print("\nExiting...")

# Exercise 4.3
print("Enter empty string to quit immediately")
inp = input("Input number:")

if inp != '':
    inp = int(inp)
    smallest = inp
    biggest = inp

    while True:
        temp_inp = input("Input number:").strip()
        if temp_inp == '':
            break
        else:
            inp = int(temp_inp)

        if inp < smallest:
            smallest = inp
        if inp > biggest:
            biggest = inp

    print("Biggest number:", biggest)
    print("Smallest number:", smallest)
    print("\n")


else:
    print("Exiting...\n")

# Exercise 4.4
from random import randint

num = randint(1, 10)
print("Enter empty string to quit")

while inp != num:
    temp_inp = input("Input number:").strip()

    if temp_inp == '':
        print("Correct answer is", num, "\n")
        break
    else:
        inp = int(temp_inp)

    if inp < num:
        print("Too low")
    elif inp > num:
        print("Too high")
    else:
        print("Correct\n")

# Exercise 4.5
username = "python"
password = "rules"

attemps = 5

while attemps > 0:
    inp_username = input("Username:")
    inp_password = input("Password:")

    if inp_username != username or inp_password != password:
        attemps = attemps - 1
        print("Incorrect. Attemps remaining:", attemps)
        if attemps == 0:
            print("Access denied\n")
            break
    elif inp_username == username and inp_password == password:
        print("Welcome\n")

# Exercise 4.6
import random
import math

pointsInsideSquare = int(input("Input number of points: "))
pointsInsideCircle = 0
i = 0

while True:
    x_axis = random.random()
    y_axis = random.random()

    if pow(x_axis, 2) + pow(y_axis, 2) < 1:
        pointsInsideCircle += 1

    if i == pointsInsideSquare - 1:
        break

    i += 1

print("pi =", 4 * pointsInsideCircle / pointsInsideSquare)
