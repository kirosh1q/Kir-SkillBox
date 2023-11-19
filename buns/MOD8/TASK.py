class Transport():
    def __init__(self, coordinates, speed, brand, year, number):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number
 
    @property
    def coordinates(self):
        return self._coordinates
 
    @coordinates.setter
    def coordinates(self, coordinates):
        self._coordinates = coordinates
 
    @property
    def speed(self):
        return self._speed
 
    @speed.setter
    def speed(self, speed):
        self._speed = speed
 
    @property
    def brand(self):
        return self._brand
 
    @brand.setter
    def brand(self, brand):
        self._brand = brand
 
    @property
    def year(self):
        return self._year
 
    @year.setter
    def year(self, year):
        self._year = year
 
    @property
    def number(self):
        return self._number
 
    @number.setter
    def number(self, number):
        self._number = number
 
    def __str__(self):
        return f'{self._brand} - {self._number}'
 
    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        return pos_x <= self._coordinates[0] <= pos_x + length and pos_y <= self._coordinates[1] <= pos_y + width
 
 
class Passenger():
    @property
    def passengers_capacity(self):
        return self._passengers_capacity
 
    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self._passengers_capacity = passengers_capacity
 
    @property
    def number_of_passengers(self):
        return self._number_of_passengers
 
    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self._number_of_passengers = number_of_passengers
 
 
class Cargo():
    @property
    def carrying(self):
        return self._carrying
 
    @carrying.setter
    def carrying(self, carrying):
        self._carrying = carrying
 
 
class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height
 
 
class Auto(Transport):
    pass
 
 
class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, name, port):
        super().__init__(coordinates, speed, brand, year, number)
        self._name = name
        self._port = port
 
 
class Car(Auto):
    pass
 
 
class Bus(Auto, Passenger):
    pass
 
 
class CargoAuto(Auto, Cargo):
    pass
 
 
class Boat(Ship):
    pass
 
 
class PassengerShip(Ship, Passenger):
    pass
 
 
class CargoShip(Ship, Cargo):
    pass
 
 
class Seaplane(Plane, Ship):
    pass


plane_instance = Plane(coordinates=(0, 0), speed=500, brand="Boeing", year=2023, number="1samolet", height=10000)
 

print(plane_instance.coordinates)  
plane_instance.coordinates = (10, 20)  
print(plane_instance.coordinates)  
 
result = plane_instance.isInArea(5, 15, 10, 10)
print(f"Плоскость в указанной области? {result}")
 
print(str(plane_instance))