#sort() method : used with lists
#sort() function : used with iterables

#if we have a list we can call the built-in sort method but with tuples and sets we need to call the "sorted" function

students = [("Spongebob", "F", "40"),
            ("Nora", "B", "20"),
            ("squidward", "A", "50"),
            ("Gharib", "A*", "55")]

grade = lambda grade: grade[1]
students.sort(key=grade)



print(students)

