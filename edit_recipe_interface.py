from data import recipes_list


def display(recipe_id):
    current_recipe = recipes_list[recipe_id]
    print("Editing", current_recipe.get_name())
    current_recipe.list_ingredients()
