import data
import ingredient
import ingredients_interface


def display():
    print("Adding new ingredient.")

    print("What is the name of the ingredient?")
    name = input()
    print("Enter the quantity and units seperated by a space (ex: 5 oz) or just a quantity: ")
    quantity_units = input().split(' ')
    quantity = quantity_units[0]
    units = None
    if len(quantity_units) > 1:
        units = quantity_units[1]

    new_ingredient = ingredient.Ingredient(name, quantity, units)
    data.ingredients_list.append(new_ingredient)

    ingredients_interface.display()
