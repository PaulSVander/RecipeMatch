class Ingredient:

    def __init__(self, name, amount, units):
        self._name = name
        self._amount = amount
        self._units = units

    def add_quantity(self, quantity):
        self._amount += quantity

    def remove_quantity(self, quantity):
        if quantity > self._amount:
            self._amount = 0
        else:
            self._amount -= quantity

    def set_name(self, name):
        self._name = name

    def set_quantity(self, quantity):
        self._amount = quantity

    def set_units(self, units):
        self._units = units

