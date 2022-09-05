#Exercise 5.1
import random

dice = int(input("Input number of dices: "))
dice_sum = 0

for i in range(dice):
    dice_num = random.randint(1, 6)
    dice_sum += dice_num

print("Sum of dice:", dice_sum)



#Exercise 5.2

