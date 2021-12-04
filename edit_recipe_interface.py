from data import recipes_list


def display_edit_recipe_interface(recipe_id):
    print('\n---------------------------\n')
    current_recipe = recipes_list[int(recipe_id) - 1]
    print("Editing\n", current_recipe.get_name())
    current_recipe.list_ingredients()

    print('0. Go Back')
    selection = input()
    if selection == '0':
        from recipes_interface import display_recipes_interface
        display_recipes_interface()