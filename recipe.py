class Recipe:

    def __init__(self, name):
        self._name = name
        self._ingredients = {}
        self._id = 0

    def set_name(self, new_name):
        self._name = new_name

    def set_id(self, new_id):
        self._id = new_id

    def get_name(self):
        return self._name

    def get_ingredients(self):
        return self._ingredients

    def add_ingredient(self, ingredient, quantity_needed, units):
        quantity_needed = str(quantity_needed)
        self._ingredients[ingredient] = quantity_needed + units

    def can_make(self):
        for ingredient in self._ingredients:
            num = ''
            for char in self._ingredients[ingredient]:
                if char.isdigit():
                    num += char
            if int(ingredient.get_amount()) < int(num):
                return False

        return True

    def make(self):
        for ingredient, quantity_needed in self._ingredients:
            ingredient.remove_quantity(quantity_needed)

    def list_ingredients(self):
        for item in self._ingredients:
            print(item.get_name(), self._ingredients[item])

    def print(self):
        print(str(self._id) + '.', self._name)


