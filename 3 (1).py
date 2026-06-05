# Mini Inventory System

products = {}

while True:

    print("\n1. Add Product")
    print("2. Show Products")
    print("3. Search Product")
    print("4. Exit")

    choice = input("Enter choice: ")

    # Add Product
    if choice == "1":

        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        products[name] = quantity

        print("Product Added!")

    # Show Products
    elif choice == "2":

        print("\nProducts List:")

        for name, quantity in products.items():

            print(name, "-", quantity)

    # Search Product
    elif choice == "3":

        search = input("Enter product name: ")

        if search in products:

            print(search, "Available")
            print("Quantity:", products[search])

        else:
            print("Product Not Found")

    # Exit
    elif choice == "4":

        print("Program Closed")
        break

    else:
        print("Invalid Choice")