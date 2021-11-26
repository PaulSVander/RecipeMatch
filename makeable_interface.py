from data import recipes_list


# Displays a list of what recipes the user can make based on the ingredients they have on hand
def display():
    print('\n---------------------------\n')
    print("Here's what you can make with your current ingredients: ")
    for recipe in recipes_list:
        if recipe.can_make():
            print(recipe.get_name())

    print("\n0. Go Back")
    selection = input()

    if selection == '0':
        from home import display
        display()