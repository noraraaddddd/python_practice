#class names use pascal notation(The first letter of each word is capitalized)
class Animal:
 alive = True
 def eat(self):
    print("is eating")
 def sleep(self):
    print("is sleeping")

class Rabbit(Animal):
 def run(self):
   print("This rabbit runs")
class Fish(Animal):
 def swim(self):
   print("This fish swims")
class Turtle(Animal):
 def walk_slowly(self):
   print("This turtle walks slowly")

rabbit = Rabbit()
fish = Fish()
turtle = Turtle()

turtle.walk_slowly()