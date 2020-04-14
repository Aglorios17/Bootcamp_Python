import sys
import datetime
from book import Book
from recipe import Recipe


a = Recipe("soupe", "1", "10",["salad", "soup"], "disgusting thing", "lunch")
recipes = {"starter": {}, "lunch": {"haha": a}, "dessert": {}}
to_print = str(a)
#print(to_print)
b = Recipe("cake", "3", "36", ["eggs", "floor"], "c est bon le cake", "dessert")
book = Book("book", datetime.date, datetime.date, recipes)
book.get_recipe_by_name("haha")
print('\n')
book.get_recipes_by_types("lunch")
book.add_recipe(b)
print('\n')
book.get_recipe_by_name("cake")
