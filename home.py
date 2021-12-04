from recipes_interface import display_recipes_interface
from ingredients_interface import display_ingredients_interface
from makeable_interface import display_makeable_interface


# "home screen"
def display_home():
    print("Welcome to Recipe Match!\n\n")
    print("1. View/Edit my ingredients")
    print("2. View/Edit my recipes")
    print("3. What can I make?")
    print("4. Exit")
    selection = int(input("\nPlease select an option: "))
    if selection == 1:
        display_ingredients_interface()
    elif selection == 2:
        display_recipes_interface()
    elif selection == 3:
        display_makeable_interface()
    elif selection == 4:
        quit()