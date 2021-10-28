import ingredient
import recipe

x = ingredient.Ingredient('banana', 20, 'lbs')
y = ingredient.Ingredient('sugar', 30, 'oz')
z = ingredient.Ingredient('salt', 50, 'g')

a = recipe.Recipe('Pie')
a.add_ingredient(x, 2, x.get_units())
a.add_ingredient(y, 5, y.get_units())

b = recipe.Recipe('Salad')
b.add_ingredient(y, 2, y.get_units())
b.add_ingredient(z, 1, z.get_units())

c = recipe.Recipe('soup')
c.add_ingredient(x, 1, x.get_units())
c.add_ingredient(y, 2, y.get_units())
c.add_ingredient(z, 3, z.get_units())

ingredients_list = [x, y, z]
recipes_list = [a, b, c]

