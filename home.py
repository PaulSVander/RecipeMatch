
# "home screen"
def display():
    print("Welcome to Recipe Match!\n\n")
    print("1. View/Edit my ingredients")
    print("2. View/Edit my recipes")
    print("3. What can I make?")
    print("4. Exit")
    selection = int(input("\nPlease select an option: "))
    if selection == 1:
        view_ingredients()
    elif selection == 2:
        view_recipes()
    elif selection == 3:
        view_makeable()
    elif selection == 4:
        quit()


def view_ingredients():
    from ingredients_interface import display
    display()


def view_recipes():
    from recipes_interface import display
    display()


def view_makeable():
    from makeable_interface import display
    display()