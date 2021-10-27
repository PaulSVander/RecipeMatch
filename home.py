import ingredients_interface


def display():
    print("Welcome to Recipe Match! Please select an option:\n\n")
    print("1. View/Edit my ingredients")
    print("2. View/Edit my recipes")
    print("3. Exit")


selection = input()

if selection == 1:
    ingredients_interface.display()

