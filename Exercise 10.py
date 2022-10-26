#Exercise 10.1
class Elevator:
    def __init__(self, floor = 0):
        self.elevator_floor = floor

    def floor_up(self):
        self.elevator_floor += 1
        print("At floor", self.elevator_floor)

    def floor_down(self):
        self.elevator_floor -= 1
        print("At floor", self.elevator_floor)

    def go_to_floor(self, desired_floor):
        if self.elevator_floor != desired_floor:
            while self.elevator_floor != desired_floor:
                if self.elevator_floor > desired_floor:
                    self.floor_down()
                elif self.elevator_floor < desired_floor:
                    self.floor_up()
        else:
            print("Already at floor", desired_floor)


h = Elevator()

h.go_to_floor(7)
print("Arrived at", h.elevator_floor)

h.go_to_floor(0)
print("Arrived at", h.elevator_floor)



#Exercise 10.2
