#Basically a concept that says the class of an object is less important than the methods/attributes of that object
#It's based on the popular phrase "if it walks like a duck and quacks like a duck then it must be a duck"

class Duck:
    def talk(self):
       print("The duck is quacking") 
        
    def walk(self):
        print("The duck is walking")
class Chicken:
    def talk(self):
        print("The chicken is clucking")
    def walk(self):
        print("The chicken can walk")

class Person:
    def catch(self, duck):
     duck.walk()
     duck.talk()
     print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()


person.catch(chicken)
