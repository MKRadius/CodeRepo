#Exercise 9.1
class Car:
    def __init__(self, reg_number: str, max_speed: int, current_speed = 0, travelled_distance = 0):
        self.registration_number = reg_number
        self.maximum_speed       = max_speed
        self.current_speed       = current_speed
        self.travelled_distance  = travelled_distance

    
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

    def accelerate(self, speed_change: int):
        if self.current_speed + speed_change > self.maximum_speed :
            self.current_speed = self.maximum_speed
        elif self.current_speed + speed_change < 0:
            self.current_speed = 0
        else:
            self.current_speed += speed_change

    def emergency_brake(self):
        print("Emergency brake")
        
        if self.current_speed > 200:
            self.current_speed -= 200
        else:
            self.current_speed = 0


new_car = Car("ABC-123", 142)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print("Current speed:", new_car.current_speed, "km/h")

new_car.emergency_brake()
print("Current speed:", new_car.current_speed, "km/h")



#Exercise 9.3
class Car:
    def __init__(self, reg_number: str, max_speed: int, current_speed = 0, travelled_distance = 0):
        self.registration_number = reg_number
        self.maximum_speed       = max_speed
        self.current_speed       = current_speed
        self.travelled_distance  = travelled_distance

    def accelerate(self, speed_change: int):
        if self.current_speed + speed_change > self.maximum_speed :
            self.current_speed = self.maximum_speed
        elif self.current_speed + speed_change < 0:
            self.current_speed = 0
        else:
            self.current_speed += speed_change

    def emergency_brake(self):
        print("Emergency brake")
        
        if self.current_speed > 200:
            self.current_speed -= 200
        else:
            self.current_speed = 0

    def drive(self, hour_driven):
        self.travelled_distance += self.current_speed * hour_driven


new_car = new_car = Car("ABC-123", 142, 60, 2000)

new_car.drive(1.5)

print("Travelled distance:", round(new_car.travelled_distance), "km")



#Exercise 9.4
import random

class Car:
    def __init__(self, reg_number: str, max_speed: int, current_speed = 0, travelled_distance = 0):
        self.registration_number = reg_number
        self.maximum_speed       = max_speed
        self.current_speed       = current_speed
        self.travelled_distance  = travelled_distance

    def accelerate(self, speed_change: int):
        if self.current_speed + speed_change > self.maximum_speed :
            self.current_speed = self.maximum_speed
        elif self.current_speed + speed_change < 0:
            self.current_speed = 0
        else:
            self.current_speed += speed_change

    def emergency_brake(self):
        print("Emergency brake")
        
        if self.current_speed > 200:
            self.current_speed -= 200
        else:
            self.current_speed = 0

    def drive(self, hour_driven):
        self.travelled_distance += self.current_speed * hour_driven


race_car = []

for i in range(10):
    name = "ABC-" + str(i + 1)
    max_speed = random.randint(100, 199)

    car_info = Car(name, max_speed)

    race_car.append(car_info)


reached_10000km = False
while not reached_10000km:
    for i in range(10):
        race_car[i].accelerate(random.randint(-10, 14))
        race_car[i].drive(1)
        
        #print(i, " ", race_car[i].travelled_distance)
        #time.sleep(0.01)
        
        if race_car[i].travelled_distance >= 10000:
            reached_10000km = True

print(" __________________________________________________________________________________________________________________________")
print("||Registration number     ||Maximum speed (km/h)      ||Current speed (km/h)       ||Travelled distance (km) ||Winner     ||")
print(" __________________________________________________________________________________________________________________________")

for i in range(10):
    print("||{0:24}||{1:26}||{2:27}||{3:24}||".format(race_car[i].registration_number, race_car[i].maximum_speed, race_car[i].current_speed, race_car[i].travelled_distance), end = '')
    if race_car[i].travelled_distance >= 10000:
        print("     X     ||")
    else:
        print("           ||")
    print(" __________________________________________________________________________________________________________________________")
