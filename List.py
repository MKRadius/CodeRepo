"""
list1 = []


match_points = [9, 4, 3, 8 , 10, 6]
i = 0

for i in match_points:
    print(i)
"""
############


shopping_list = ["pencil", "eraser", "books", "books", "pen", 3, 5]
print(shopping_list)
shopping_list[3] = "food"
shopping_list[5] = 45
print(shopping_list)

"""
number_list = []

number_list.append(1)
number_list.append(2)
number_list.append(5)

print(number_list)
"""

shopping_list.insert(2, "apple")
print(shopping_list)

shopping_list.remove("eraser")
print(shopping_list)

shopping_list.pop(5)
shopping_list.pop(4)
print(shopping_list)
