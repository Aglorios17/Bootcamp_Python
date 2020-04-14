class Book:
	def __init__(self, name, last_update, creation_date, recipe_list):
		self.name = name
		self.last_update = last_update
		self.creation_date = creation_date
		self.recipes_list = recipe_list#{
			#	'starte':[],
			#	'lunch':[],
			#	'dessert':[],
#		}

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		for key, val in self.recipes_list.items():
			for a, b in val.items():
				if name == a:
					print(str(b))

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """ 
		for key, val in self.recipes_list.items():
			if key == recipe_type:
				for a, b in val.items():
					print(str(b))

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update""" 
		pass
