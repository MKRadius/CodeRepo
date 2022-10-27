#Exercise 10.1
class Elevator:
    def __init__(self, bottom_floor: int, top_floor: int):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.elevator_floor = bottom_floor

    def floor_up(self):
        self.elevator_floor += 1
        
    def floor_down(self):
        self.elevator_floor -= 1

    def go_to_floor(self, desired_floor):
        if self.elevator_floor != desired_floor:
            if self.bottom_floor <= desired_floor <= self.top_floor:
                
                while self.elevator_floor != desired_floor:
                    if self.elevator_floor > desired_floor:
                        self.floor_down()
                    elif self.elevator_floor < desired_floor:
                        self.floor_up()
                
                #Went to desired floor
                print("At floor", self.elevator_floor)
            else:
                print("Can't go to unexisted floor")
        else:
            print("Already at floor", desired_floor)


h = Elevator(0, 10)

h.go_to_floor(5)
print("Arrived at", h.elevator_floor)

h.go_to_floor(11)
print("Arrived at", h.elevator_floor)

h.go_to_floor(0)
print("Arrived at", h.elevator_floor)



#Exercise 10.2
class Elevator:
    def __init__(self, bottom_floor: int, top_floor: int):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.elevator_floor = bottom_floor

    def floor_up(self):
        self.elevator_floor += 1
        
    def floor_down(self):
        self.elevator_floor -= 1

    def go_to_floor(self, desired_floor):
        if self.elevator_floor != desired_floor:
            if self.bottom_floor <= desired_floor <= self.top_floor:
                
                while self.elevator_floor != desired_floor:
                    if self.elevator_floor > desired_floor:
                        self.floor_down()
                    elif self.elevator_floor < desired_floor:
                        self.floor_up()
                
                #Went to desired floor
                print("At floor", self.elevator_floor)
            else:
                print("Can't go to unexisted floor")
        else:
            print("Already at floor", desired_floor)

class Building:
    def __init__(self, bottom_floor: int, top_floor: int, elevator_count = 3):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_count = elevator_count
        self.elevators = []
        
        for i in range(self.elevator_count):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)
    
    def run_elevator(self, elevator_no, desired_floor):
        print("Run elevator no." + str(elevator_no))
        if elevator_no - 1 > self.elevator_count:
            print("Can't run unexisted elevator")
        else:
            self.elevators[elevator_no - 1].go_to_floor(desired_floor)
        

landmark81 = Building(0, 81, 5)

landmark81.run_elevator(2, 30)
landmark81.run_elevator(1, 100)
landmark81.run_elevator(5, 81)



#Exercise 10.3
class Elevator:
    def __init__(self, bottom_floor: int, top_floor: int):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.elevator_floor = bottom_floor

    def floor_up(self):
        self.elevator_floor += 1
        
    def floor_down(self):
        self.elevator_floor -= 1

    def go_to_floor(self, desired_floor):
        if self.elevator_floor != desired_floor:
            if self.bottom_floor <= desired_floor <= self.top_floor:
                
                while self.elevator_floor != desired_floor:
                    if self.elevator_floor > desired_floor:
                        self.floor_down()
                    elif self.elevator_floor < desired_floor:
                        self.floor_up()
                
                #Went to desired floor
                print("At floor", self.elevator_floor)
            else:
                print("Can't go to unexisted floor")
        else:
            print("Already at floor", desired_floor)

class Building:
    def __init__(self, bottom_floor: int, top_floor: int, elevator_count = 3):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_count = elevator_count
        self.elevators = []
        
        for i in range(self.elevator_count):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)
    
    def run_elevator(self, elevator_no, desired_floor):
        print("Run elevator no." + str(elevator_no))
        if elevator_no - 1 > self.elevator_count:
            print("Can't run unexisted elevator")
        else:
            self.elevators[elevator_no - 1].go_to_floor(desired_floor)

    def fire_alarm(self):
        for i in range(self.elevator_count):
            print("Run elevator no." + str(i + 1))
            self.elevators[i].go_to_floor(0)
        print("All elevators at bottom floor")
        

landmark81 = Building(-5, 81, 5)

landmark81.run_elevator(1, 100)
landmark81.run_elevator(1, 10)
landmark81.run_elevator(1, 20)
landmark81.run_elevator(2, 30)
landmark81.run_elevator(3, -3)
landmark81.run_elevator(5, 81)
print("")

landmark81.fire_alarm()



#Exercise 10.4
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

class Race:
    def __init__(self, name, distance, race_car, finish_line_reached = False):
        self.race_name = name
        self.race_distance = distance
        self.cars = race_car
        self.finish_line_reached = finish_line_reached

    def hour_passes(self):
        for i in range(10):
            race_car[i].accelerate(random.randint(-10, 14))
            race_car[i].drive(1)
        
            #print(i, " ", race_car[i].travelled_distance)
            #time.sleep(0.01)
        
            if race_car[i].travelled_distance >= self.race_distance:
                self.finish_line_reached = True
        
        return 1

    def print_status(self):
        print(" __________________________________________________________________________________________________________________________")
        print("||Registration number     ||Maximum speed (km/h)      ||Current speed (km/h)       ||Travelled distance (km) ||Winner     ||")
        print(" __________________________________________________________________________________________________________________________")

        for i in range(10):
            print("||{0:24}||{1:26}||{2:27}||{3:24}||".format(self.cars[i].registration_number, self.cars[i].maximum_speed, self.cars[i].current_speed, self.cars[i].travelled_distance), end = '')
            if self.cars[i].travelled_distance >= self.race_distance:
                print("     X     ||")
            else:
                print("           ||")
            print(" __________________________________________________________________________________________________________________________")

    def race_finished(self):
        return self.finish_line_reached

race_car = []

for i in range(10):
    name = "ABC-" + str(i + 1)
    max_speed = random.randint(100, 199)
    car_info = Car(name, max_speed)
    race_car.append(car_info)

gdb_race = Race("Grand Demolition Derby", 8000, race_car)
race_hours = 0

while not gdb_race.race_finished():
    
    race_hours += gdb_race.hour_passes()
    if race_hours % 10 == 0:
        gdb_race.print_status()
        print("Time elapsed:", race_hours)
        input("Enter to continue...")

gdb_race.print_status()
