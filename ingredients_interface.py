import add_ingredient_interface
import home
import ingredient
import data


def display():
    print("Here are the ingredients you have on hand: ")
    for ingredient_id in range(1, len(data.ingredients_list)):
        data.ingredients_list[ingredient_id].id = ingredient_id
        data.ingredients_list[ingredient_id].print()
    print("Select an ingredient to edit, or enter 'new' to add an ingredient: ")


selection = input()

if selection == 0:
    home.display()
elif selection == 'new':
    add_ingredient_interface.display()
else:
    edit_ingredient_interface.display(selection)
