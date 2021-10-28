# import edit_ingredient_interface
import home
# import ingredient
from data import ingredients_list


def display():
    print("Here are the ingredients you have on hand: \n")
    print("0. Go Back\n")
    for ingredient_id in range(0, len(ingredients_list)):
        ingredients_list[ingredient_id].set_id(ingredient_id + 1)
        ingredients_list[ingredient_id].print()
    print("Select an ingredient to edit, or enter 'new' to add an ingredient: ")

    selection = input()

    if selection == '0':
        home.display()
    elif selection == 'new':
        from add_ingredient_interface import display
        display()
    else:
        from edit_ingredient_interface import display
        display(selection)
