class Recipe:

    def __init__(self, name):
        self._name = name
        self._ingredients = {}

    def set_name(self, new_name):
        self._name = new_name

    def add_ingredient(self, ingredient, quantity_needed):
        self._ingredients[ingredient] = quantity_needed

    def can_make(self):
        for ingredient, quantity_needed in self._ingredients:
            if ingredient.get_amount() < quantity_needed:
                return False

        return True

    def makee(self):
        for ingredient, quantity_needed in self._ingredients:
            ingredient.remove_quantity(quantity_needed)


