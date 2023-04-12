#reduce() applies a function to the first two elements of an iterable and continues doing so until we reach one cumalitive value
#reduce(function, iterable)

import functools

# letters = ["H","E","L","L","O"]
# result_1 = functools.reduce(lambda z, x: z+x, letters)
# print(result_1)

factorial = [1, 2, 3, 4, 5]
#starts multiplying the first two elements until it's left with a single value
result = functools.reduce(lambda x,y : x*y, factorial)

print(result)

