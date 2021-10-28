from data import recipes_list


def display():
    print("Here's what you can make with your current ingredients: ")
    for recipe in recipes_list:
        if recipe.can_make():
            print(recipe.get_name())
