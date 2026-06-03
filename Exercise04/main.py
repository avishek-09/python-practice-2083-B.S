# practice for the dictionery a program for tea shop 

menu = {"milk tea":40,
        "black tea":35,
        "lemon tea":3,
        "cookies":50,
        "lemonade":110,
        "bread toast":120,
        "green tea":45,
        "milk coffee":80,
        "black coffee":70,
        "fruit juice":150,
        }
cart = []
total = 0

print("------- Menu -------")
for key , value in menu.items():
    print(f"{key:15}:Rs.{value}")
print("--------------------")

while True:
    choose = input("Enter the items you want(q to quit) :").lower()
    if choose == "q":
        break
    elif menu.get(choose) is not None:
        cart.append(choose)

print("---Your Order---")
for choose in cart:
    total += menu.get(choose)
    print(choose, end=" ")
    print()
print("----------------")
print(f"Your sum total is Rs.{total}")