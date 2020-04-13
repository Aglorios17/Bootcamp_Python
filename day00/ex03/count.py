import sys

def text_analyzer(*args):
	""" analyser un texte et renvoyer le nombre de maj, min, espace,.."""
	upper = 0;
	lower = 0;
	spaces = 0;
	numbers = 0;
	i = len(args)
	if i != 1:
		print("What is the text to analyse?")
		return
	else:
		str = args[0]
		characters = len(str)
		i = 0;
		while i < characters:
			if str[i].islower() is True:
				lower += 1
			elif str[i].isupper() is True:
				upper += 1
			elif str[i] == ' ':
				spaces += 1
			elif str[i].isdigit():
				numbers += 1
			i += 1
		punctuation = characters - (lower + upper + spaces + numbers)
		print("The text contains ",characters, "characters :", end='\n\n')	
		print("-",upper, "upper letters", end='\n\n')			
		print("-",lower, "lower letters", end='\n\n')
		print("-",punctuation, "ponctuation marks", end='\n\n')
		print("-",spaces, "spaces", end='\n\n')
