import ingredient
import recipe

x = ingredient.Ingredient('banana', 20, 'lbs')
y = ingredient.Ingredient('sugar', 30, 'oz')
z = ingredient.Ingredient('salt', 50, 'g')

a = recipe.Recipe('Pie')
a.add_ingredient(x, 2)
a.add_ingredient(y, 5)

b = recipe.Recipe('Salad')
b.add_ingredient(y, 2)
b.add_ingredient(z, 1)

c = recipe.Recipe('soup')
c.add_ingredient(a, 1)
c.add_ingredient(b,2)
c.add_ingredient(c, 3)

ingredients_list = [x, y, z]
recipes_list = [a, b, c]

