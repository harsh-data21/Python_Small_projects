print("\n == MINI SHOPPING CART ===")

products = ["Rice", "Bread", "Milk", "Wheat"]
prices = [20, 30, 35, 40]

cart = []
total = 0

while True:
    print("\nAvailable products:")

    for i in range(len(products)):
        print(i + 1, "._.", products[i], "-RS", prices[i])

    print("5. Exit")
    choice = int(input("Enter product no: "))

    if choice >= 1 and choice <= 4:
        cart.append(products[choice - 1])
        total = total + prices[choice - 1]
        print(products[choice - 1], "Added to Cart")

    elif choice == 5:
        break

    else:
        print("Invalid Choice")

    print("\n == Your Cart == ")

    if len(cart) == 0:
        print("Cart is empty")
    else:
        for items in cart:
            print("_", items)

        print("Total amount = RS", total)

print("Thank you for Shopping")
