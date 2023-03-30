#shopping cart program 

foods = []
prices = []
total = 0

while True: 
 food = input("What food would you like to buy?(enter q to quit):")
 if food.lower() == "q":
    break
 else:
    foods.append(food)
    price = float(input(f"Enter the price of a {food}:"))
    prices.append(price)

for price in prices:
 total += price

print("-----YOUR CART-----")

for food in foods:
  print(food, end = " ")


print(f"\nYour total is {total}$\n")



