#filter() creates a collection of elements from an iterable that return true for an expression
#filter(function, iterable)

friends = [("Rose", 19),
           ("Parmin", 17),
           ("Paria", 15),
           ("Soheil", 25),
           ("Mahsa", 19),
           ("Tom", 2)]

age = lambda age: age[1] >=18

drinking_buddies = filter(age, friends)
for i in drinking_buddies:
    print(i)