import recipe
import recipes_interface
from data import recipes_list
from data import ingredients_list
import json
import scraper_connection


def display():
    print("\nAdding a new recipe")
    print("Enter the recipe name, or 'cancel' to cancel recipe entry")
    name = input("Recipe Name: ")
    if name == 'cancel':
        recipes_interface.display()
    new_recipe = recipe.Recipe(name)
    add_ingredients(new_recipe)

    recipe_image = image_request(new_recipe)

    recipes_list.append(new_recipe)

    from recipes_interface import display
    display()


def add_ingredients(current_recipe):
    selection = ''
    while selection != 'done':

        for ingredient_id in range(0, len(ingredients_list)):
            ingredients_list[ingredient_id].set_id(ingredient_id + 1)
            ingredients_list[ingredient_id].print()
        print(
            "\nSelect ingredient to add to recipe, or enter 'done' to finish recipe entry, or 'cancel' to cancel recipe entry")
        selection = input()
        if selection == 'done':
            break
        elif selection == 'cancel':
            recipes_interface.display()
        else:
            selection = int(selection)
        selected_ingredient = ingredients_list[selection - 1]
        print("\nEnter the quantity of", selected_ingredient.get_name(), "needed (number only, without units (ex. 5))")
        quantity = input()

        current_recipe.add_ingredient(selected_ingredient, quantity, selected_ingredient.get_units())

    print("\nRecipe added!")


def image_request(recipe):
    print("Would you like to add an image for this recipe?\n")
    print("1. Yes\n2. No\n")
    selection = input()

    if selection == '1':
        print("Retrieving image...\n")
        image = retrieve_image(recipe.get_name())
        recipe.set_img_url(image)

    recipes_interface.display()


def retrieve_image(recipe_name):
    recipe_name = str(recipe_name).replace(" ", "+")
    url = "https://www.allrecipes.com/search/results/?search=" + recipe_name

    # Send the page to scrape in JSON format
    message = {"URL": url}
    json_message = json.dumps(message)
    encoded_json_message = json_message.encode('utf-8')
    encoded_msg_len = len(encoded_json_message)
    encoded_len_str = str(encoded_msg_len).encode('utf-8')
    len_buffered = encoded_len_str + b' ' * (64 - len(encoded_len_str))

    response = scraper_connection.connect_to_scraper(len_buffered, encoded_json_message)
    response_list = response.split(',')

    print("Would you like to use this image: ")
    print(response_list[30])
    print('\n1. Yes\n2. No')
    selection = input()

    if selection == '1':
        return response_list[30]
    else:
        return None