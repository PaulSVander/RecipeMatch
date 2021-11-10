import ingredient
import data
import ingredients_interface


def display(ingredient_id):
    print('\n---------------------------\n')
    print("Editing ingredient")
    ingredient_id = int(ingredient_id) - 1
    current_ingredient = data.ingredients_list[ingredient_id]
    print(current_ingredient.get_name(), current_ingredient.get_amount(), current_ingredient.get_units())
    print("\n0. Go back\n\n1. Edit name\n2. Edit quantity\n3. Edit units\n4. Delete ingredient\n")

    print("Please select an option: ")
    selection = input()

    if selection == '1':
        new_name = input("Enter a new name: ")
        current_ingredient.set_name(new_name)
        print("Name updated")
    elif selection == '2':
        new_quantity = input("Enter a new quantity: ")
        current_ingredient.set_quantity(new_quantity)
        print("Quantity updated")
    elif selection == '3':
        units = input("Enter a new unit type, or 0 to remove the unit type: ")
        if units == 0:
            units = None
        current_ingredient.set_units(units)
        print("Units updated")
    elif selection == '4':

        print('Are you sure you want to delete this ingredient?\n')
        print('1. Yes\n2. No')
        choice = input()
        if choice == '2':
            display(int(ingredient_id) + 1)
        data.ingredients_list.remove(current_ingredient)
        print("Ingredient deleted")
        ingredients_interface.display()
    elif selection == '0':
        ingredients_interface.display()

    display(int(ingredient_id) + 1)

