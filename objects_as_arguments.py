#This program aims to show how we can create objects and then pass them as arguments in a separate function
class Car:
    colour = None
class Motorcycle:
    colour = None

def change_colour(car, colour):

    car.colour = colour

car_1 = Car
car_2 = Car
car_3 = Car
motorcycle_1 = Motorcycle
Motorcycle_2 = Motorcycle

change_colour(car_1,"purple")
change_colour(car_2,"white")
change_colour(car_3,"green")

change_colour(motorcycle_1,"green")
change_colour(Motorcycle_2,"black")

print(car_1.colour)
print(car_2.colour)
print(car_3.colour)
print(motorcycle_1.colour)
print(Motorcycle_2.colour)