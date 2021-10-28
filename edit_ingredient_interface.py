import ingredient
import data
import ingredients_interface


def display(ingredient_id):
    print("Editing ingredient")
    current_ingredient = data.ingredients_list[ingredient_id]
    current_ingredient.print()

    print("Please select an option: ")
    print("1. Edit name\n2. Edit quantity\n3. Edit units\n. Delete ingredient\n5. Go back")
    selection = input()

    if selection == 1:
        current_ingredient.set_name = input("Enter a new name: ")
        print("Name updated")
    elif selection == 2:
        current_ingredient.set_quantity = input("Enter a new quantity: ")
        print("Quantity updated")
    elif selection == 3:
        units = input("Enter a new unit type, or 0 to remove the unit type: ")
        if units == 0:
            units = None
        current_ingredient.set_units = units
        print("Units updated")
    elif selection == 4:
        del current_ingredient
        print("Ingredient deleted")
    elif selection == 5:
        ingredients_interface.display()

    display(ingredient_id)

