import recipe

from data import recipes_list
from data import ingredients_list


def display():
    print("\nAdding a new recipe")
    name = input("Enter the recipe name: ")
    new_recipe = recipe.Recipe(name)
    add_ingredients(new_recipe)

    recipes_list.append(new_recipe)
    from recipes_interface import display
    display()


def add_ingredients(current_recipe):
    selection = ''
    while selection != 'done':

        print("\nSelect ingredient to add to recipe, or enter 'done' to finish recipe entry")
        for ingredient_id in range(0, len(ingredients_list)):
            ingredients_list[ingredient_id].set_id(ingredient_id + 1)
            ingredients_list[ingredient_id].print()
        selection = input()
        if selection == 'done':
            break
        else:
            selection = int(selection)
        selected_ingredient = ingredients_list[selection - 1]
        quantity = input("\nEnter the quantity needed: ")

        current_recipe.add_ingredient(selected_ingredient, quantity)
