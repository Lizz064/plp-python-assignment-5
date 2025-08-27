# Parent Class
class Vehicle:
    def move(self):
        pass 


# Child Classes
class Car(Vehicle):
    def move(self):
        return "Driving "


class Plane(Vehicle):
    def move(self):
        return "Flying "


class Boat(Vehicle):
    def move(self):
        return "Sailing "


class Bicycle(Vehicle):
    def move(self):
        return "Pedaling "


# Create a list of vehicles
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Loop through and call move()
for v in vehicles:
    print(v.move())
