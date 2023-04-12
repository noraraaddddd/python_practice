#list comprehension = a way to create a new list with less syntax
#it can mimic certain lambda functions and is easier to read
#list = [expression for item in iterable]
#list = [expression for item in iterable if conditional]
#list = [expression if/else for item in iterable]

# #same code but the second one is a lot clearer
# squares = []
# for i in range(1,10):
#   squares.append(i*i)
# print(squares)

# squares = [i*i for i in range(1,10)]
# print(squares)

students = [0,30,70,60,55,40,100]

passed_students = [i if i>=60 else "FAILED" for i in students ]

for i in passed_students:
    print(i)