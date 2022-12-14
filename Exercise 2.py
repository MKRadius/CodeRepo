#Exercise 2.1
name = input("What's your name?\n")
print("Hello, " + name + "!\n")

#Exercise 2.2
import math
radius = input("Input radius: ")
area = math.pi * pow(float(radius), 2)
print(f"The area of the circle is {area:.3f}")

#Exercise 2.3
length = float(input("Input rectangle's length: "))
width = float(input("Input rectangle's width: "))

print("The perimeter is", (length + width) * 2, "and the area is", length * width)

#Exercise 2.4
num1 = int(input("Input first int:"))
num2 = int(input("Input second int:"))
num3 = int(input("Input third int:"))

print("Sum:", num1 + num2 + num3, "\nProduct:", num1 * num2 * num3, "\nAverage:", f"{float((num1 + num2 + num3) / 3):.3f}")

#Exercise 2.5
talents = input("Enter talents:\n")
pounds = input("Enter pounds:\n")
lots = input("Enter lots:\n")

f_tl = float(talents)
f_pnds = float(pounds) + f_tl * 20
f_lots = float(lots) + f_pnds * 32

print("The weight in modern units:")
print(int(f_lots * 13.3 // 1000), "kilograms and", f"{f_lots * 13.3 % 1000:.2f}", "grams.\n")

#Exercise 2.6
import random
print("First lock: " + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)))
print("Second lock: " + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6))+ str(random.randint(1, 6)))
