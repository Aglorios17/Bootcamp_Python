class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		try:
			self.name = str(name)
			self.cooking_level = int(cooking_lvl)
			self.cooking_time = int(cooking_time)
			self.ingredients = list(ingredients)
			self.description = str(description)
			self.recipe_type = str(recipe_type)
		except ValueError as ve:
			print(f"Invalid integer: {ve.args[0][ve.args[0].find(': ')+2:]}")
		if name == '' or str == '':
			print("cant accept empty lists")
	
	def __str__(self):
		txt = "name:{0}\ncooking level:{1}\ncooking time:{2}\ningredients:{3}\ndescription:{4}\nrecipe_type:{5}".format(self.name, self.cooking_level, self.cooking_time, self.ingredients, self.description, self.recipe_type)
		return txt
