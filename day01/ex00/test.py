import sys
import datetime
from book import Book
from recipe import Recipe


a = Recipe("haha", "1", "10",["salad", "soup"], "disgusting thing", "lunch")
recipes = {"starter": {}, "lunch": {"haha": a}, "dessert": {}}
to_print = str(a)
#print(to_print)
book = Book("book", datetime.date, datetime.date, recipes)
book.get_recipe_by_name("haha")
book.get_recipes_by_types("lunch")
