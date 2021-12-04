import home
from data import ingredients_list
from edit_ingredient_interface import display_edit_ingredient_interface


# Main ingredients interface to add or edit ingredients
def display_ingredients_interface():
    print('\n---------------------------\n')
    print("Here are the ingredients you have on hand: \n")
    print("0. Go Back\n")
    for ingredient_id in range(0, len(ingredients_list)):
        ingredients_list[ingredient_id].set_id(ingredient_id + 1)
        ingredients_list[ingredient_id].print()
    print("\nSelect an ingredient to edit, or enter 'new' to add an ingredient: ")

    selection = input()

    if selection == '0':
        home.display_home()
    elif selection == 'new':
        from add_ingredient_interface import display_add_ingredient_interface
        display_add_ingredient_interface()
    else:
        display_edit_ingredient_interface(selection)