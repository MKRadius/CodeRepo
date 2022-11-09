#Exercise 11.1
class publication:
    def __init__(self, name: str):
        self.name = name

class book(publication):
    def __init__(self, name, author: str, page_count: int):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"Book: {self.name}, {self.page_count} pages \nAuthor: {self.author}")

class magazine(publication):
    def __init__(self, name, chief: str):
        self.chief_editor = chief
        super().__init__(name)

    def print_information(self):
        print(f"Magazine: {self.name} \nChief editor: {self.chief_editor}")


pub1 = magazine("Donald Duck", "Aki Hyyppä")
pub2 = book("Compartment No. 6", "Rosa Liksom", 192)

pub1.print_information()
print("")
pub2.print_information()



#Exercise 11.2
class Car:
    def __init__(self, reg_num: str, max_speed: str, distance = 0):
        self.registration_number = reg_num
        self.maximum_speed = max_speed
        self.driven_distance = distance
    
    def drive(self, speed: int, time: int):
        if speed < 0 or speed > self.maximum_speed:
           print("Can't drive at " + str(speed) + "km/h") 
        else:
            print("Drive at " + str(speed) + "km/h for " + str(time) + "h")
            self.driven_distance += speed * time

class ElectricCar(Car):
    def __init__(self, reg_num, max_speed, battery: int):
        self.battery_capacity = battery
        super().__init__(reg_num, max_speed)

class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, gas: int):
        self.tank_capacity = gas
        super().__init__(reg_num, max_speed)

tesla = ElectricCar("ABC-15", 180, 52.5)
bmw = GasolineCar("ACD-123", 165, 32.3)

tesla.drive(140, 3)
tesla.drive(200, 3)
tesla.drive(50, 3)
print("Electric car driven distance:", str(tesla.driven_distance) + "km")

bmw.drive(-5, 3)
bmw.drive(150, 3)
bmw.drive(70, 3)
print("Gasoline car driven distance:", str(bmw.driven_distance) + "km")
