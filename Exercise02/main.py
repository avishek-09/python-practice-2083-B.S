# A Shopping Cart program to understand the use of list and user inputs 

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want to buy(press q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price : Nrs."))
        prices.append(price)
        foods.append(food)

print("---- Your Cart------")
for food in foods:
    print(food)

for price in prices:
    total += price

print()
print(f"Your amount total is Nrs.{total}")