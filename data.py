import ingredient
import recipe

x = ingredient.Ingredient('banana', 20, 'lbs')
y = ingredient.Ingredient('sugar', 30, 'oz')
z = ingredient.Ingredient('salt', 50, 'g')
x2 = ingredient.Ingredient('cinamon', 2, 'cups')
y2 = ingredient.Ingredient('basil', 10, 'g')
z2 = ingredient.Ingredient('bellpepper', 5, 'oz')

a = recipe.Recipe('Pie')
a.add_ingredient(x, 2, x.get_units())
a.add_ingredient(y, 5, y.get_units())

b = recipe.Recipe('Salad')
b.add_ingredient(y, 2, y.get_units())
b.add_ingredient(z, 1, z.get_units())

c = recipe.Recipe('soup')
c.add_ingredient(x, 1245, x.get_units())
c.add_ingredient(y, 2, y.get_units())
c.add_ingredient(z, 3, z.get_units())

ingredients_list = [x, y, z, x2, y2, z2]
recipes_list = [a, b, c]

