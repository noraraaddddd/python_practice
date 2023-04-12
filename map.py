#map() applies a function to each item in an iterable(lists, tuples, sets, etc.)
#map(function, iterable)

store = [("shirt", 20),
         ("pants", 30),
         ("socks", 10),
         ("sweater", 35)]

to_euros = lambda data :(data[0],int(data[1]*0.82)) 
store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)