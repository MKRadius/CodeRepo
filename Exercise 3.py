#Exercise 3.1
z_size = int(input("Input zander length (in cm): "))

if z_size >= 42:
    print("You caught a", z_size, "cm zander")
else:
    print("Zander too small. Realease the zander back to the lake.")


#Exercise 3.2
c_class = input("Input cabin class: ").strip()

if c_class == "LUX":
    print("Upper-deck cabin with a balcony")
elif c_class == "A":
    print("Above the car deck, equipped with a window")
elif c_class == "B":
    print("Windowless cabin above the car deck")
elif c_class == "C":
    print("Windowless cabin below the car deck")
else:
    print("Invalid cabin class")


#Exercise 3.3
gender = input("Input youe biological gender (Male/Female): ").strip()
hem_value = float(input("Input your hemoglobin: "))

if gender == "Male":
    if 134 <= hem_value <= 167:
        print("Your hemoglobin value is normal")
    elif hem_value < 134:
        print("Your hemoglobin value is low")
    else:
        print("Your hemoglobin value is high")

if gender == "Female":
    if 117 <= hem_value <= 155:
        print("Your hemoglobin value is normal")
    elif hem_value < 117:
        print("Your hemoglobin value is low")
    else:
        print("Your hemoglobin value is high")


#Exercise 3.4
year = int(input("Input year: "))

if year % 4 == 0 and year % 100 != 0:
    print("The year", year, "is a leap year")
elif year % 4 == 0 and year % 400 == 0:
    print("The year", year, "is a leap year")
else:
    print("The year", year, "is not a leap year")
