import sys

cookbook = {
	'sandwich' :{ 
		'ingredients' : ['ham', 'brad', 'cheese', 'tomatoes'],
		'meal' : 'lunch',
		'prep_time' : '10',
	},
	'cake' :{
		'ingredients' : ['flour', 'sugar', 'eggs'],
		'meal' : 'dessert',
		'prep_time' : '60',
	},
	'salad' :{
		'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
		'meal' : 'lunch',
		'prep_time' : '15',
	},
}
again = True
while again:
	print("Please select an option by typing the corresponding number:")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")
	
	a = input(">> ")
	
	if a == '5':
		print('\n')
		print("Cookbook closed.")
		again = False
					
	elif a == '4':
		print("\n------COOKBOOK------\n")
		for key, val in cookbook.items():
			print("{:.^20}".format(key))
	
	elif a == '3':
		recipe = input("\nPlease enter the recipe's name to get its details:\n>>")
		if recipe in cookbook:
			for key, val in cookbook.items():
				if key == recipe:
					print("####################################")
					print("\nRecipe for", key)
					print("Ingredient list : {}\nTo be eaten for {}.\nTakes {} minutes of cooking.".format(*val.values()))
					print("\n####################################")

	elif a == '2':
		recipe = input("\nPlease enter the recipe's name to delete:\n>>")
		for key in list(cookbook):
			if key == recipe:
				cookbook.pop(key)
				print("\nDELETED")
				print("\n--UPDATED COOKBOOK--")
				for key, val in cookbook.items():
					print("{:.^20}".format(key))
	elif a == '1':
		recipe = input("\nPlease enter the recipe's name to add:\n>>")
		ingredients = []
		while True:
			ing = input("\nPlease enter the ingredients to add(tap 1 to stop):\n>>")
			if ing.isdigit() and int(ing) == 1:
				break
			ingredients.append(ing)	
		print(ingredients)
		meal = input("\nPlease enter the meal:\n>>")
		time = input("\nPlease enter preparation time:\n>>")
		cookbook[recipe] = {'ingredients': ingredients, 'meal': meal, 'prep_time':time}
		print("\n--UPDATED COOKBOOK--")
		for key, val in cookbook.items():
			print("{:.^20}".format(key))
	print('\n')
