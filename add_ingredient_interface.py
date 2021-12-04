import data
import ingredient
import ingredients_interface


def display_add_ingredient_interface():
    print("Adding new ingredient.")

    print("What is the name of the ingredient? (Enter 'cancel' to cancel this entry)")
    name = input("Ingredient name: ")
    if name == 'cancel':
        ingredients_interface.display_ingredients_interface()
    print("Enter the quantity and units seperated by a space (ex: 5 oz). (Enter 'cancel' to cancel "
          "this entry)")
    quantity_units = input("Quantity: ").split(' ')
    # Store quantiy and units as separate variables to allow easier editing
    quantity = quantity_units[0]
    if quantity == 'cancel':
        ingredients_interface.display_ingredients_interface()
    units = None
    if len(quantity_units) > 1:
        units = quantity_units[1]

    new_ingredient = ingredient.Ingredient(name, quantity, units)
    data.ingredients_list.append(new_ingredient)

    ingredients_interface.display_ingredients_interface()