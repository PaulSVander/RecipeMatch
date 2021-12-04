from data import recipes_list
from add_recipe_interface import display_add_recipe_interface
from edit_recipe_interface import display_edit_recipe_interface


# Main recipes page where recipes can be edited or added
def display_recipes_interface():
    print('\n---------------------------\n')
    print("Here are the recipes in your book: \n")
    print("0. Go Back\n")
    for recipe_id in range(0, len(recipes_list)):
        recipes_list[recipe_id].set_id(recipe_id + 1)
        recipes_list[recipe_id].print()
    print("\nSelect a recipe to edit, or enter 'new' to add a new recipe: ")

    selection = input()

    if selection == '0':
        from home import display_home
        display_home()
    elif selection == 'new':
        display_add_recipe_interface()
    else:
        display_edit_recipe_interface(int(selection))