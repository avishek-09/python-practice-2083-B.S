# A Shopping Cart program to understand the use of list and user inputs 

Foods = []
price = []
total = 0

while True:
    Food = input("Enter the food you want to buy(press q to quit): ")
    if Food.lower() == "q":
        break
    else:
        Foods.append(Food)

print("---- Your Cart------")
for Food in Foods:
    print(Food)