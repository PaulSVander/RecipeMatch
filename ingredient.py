class Ingredient:

    def __init__(self, name, amount, units=None):
        self._name = name
        self._amount = amount
        self._units = units
        self._id = 0

    def add_quantity(self, quantity):
        self._amount += quantity

    def remove_quantity(self, quantity):
        if quantity > self._amount:
            self._amount = 0
        else:
            self._amount -= quantity

    def set_id(self, new_id):
        self._id = new_id

    def set_name(self, new_name):
        self._name = new_name

    def set_quantity(self, new_quantity):
        self._amount = new_quantity

    def set_units(self, new_units):
        self._units = new_units

    def get_name(self):
        return self._name

    def get_amount(self):
        return self._amount

    def get_units(self):
        return self._units

    def print(self):
        print(self._id, ". ", self._name, '\t', self._amount, self._units)

