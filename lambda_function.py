#lambda function in a function written in one line using the lambda keyword
#accepts any number of arguments but only has one expression(think of it as a shortcut)
#useful if it's needed for a short period of time and then gets thrown away
#lambda parameters: expression


double = lambda x: x*2
multiply = lambda x,y : x*y
add = lambda x, y, z: x+y+z
age_check = lambda age: True if age >= 18 else False

print(age_check(4))