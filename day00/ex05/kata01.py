import sys

languages = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}

for key,val in languages.items(): 
	print(key, "was created by", val)
