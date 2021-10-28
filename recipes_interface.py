from data import recipes_list


def display():
    print("Here are the recipes in your book: ")
    for recipe_id in range(0, len(recipes_list)):
        recipes_list[recipe_id].set_id(recipe_id + 1)
        recipes_list[recipe_id].print()
    print("Select a recipe to edit, or enter new to add a new ingredient: ")

    selection = input()

    if selection == 0:
        from home import display
        display()
    elif selection == 'new':
        from add_recipe_interface import display
        display()
    else:
        from edit_recipe_interface import display
        display(selection)
