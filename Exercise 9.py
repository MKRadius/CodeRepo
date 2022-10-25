#Exercise 9.1
class Car:
    def __init__(self, reg_number: str, max_speed: int, current_speed = 0, travelled_distance = 0):
        self.registration_number = reg_number
        self.maximum_speed       = max_speed
        self.current_speed       = current_speed
        self.travelled_distance  = travelled_distance

        return
    
    
new_car = Car("ABC-123", 142)

#print(vars(new_car))

#import pprint
#pprint.pprint(vars(new_car))

print("Properties of the new car")
print("Registration number  :", new_car.registration_number)
print("Maximum speed        :", new_car.maximum_speed, "km/h")
print("Current speed        :", new_car.current_speed, "km/h")
print("Travelled distance   :", new_car.travelled_distance, "km")



#Exercise 9.2
class Car:
    def __init__(self, reg_number: str, max_speed: int, current_speed = 0, travelled_distance = 0):
        self.registration_number = reg_number
        self.maximum_speed       = max_speed
        self.current_speed       = current_speed
        self.travelled_distance  = travelled_distance

        return