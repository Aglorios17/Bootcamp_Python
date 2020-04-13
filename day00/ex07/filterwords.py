import sys

i = len(sys.argv)
if i == 3:
	if sys.argv[2].isdigit() is True and sys.argv[1].isdigit() is False:
		words = []
		wordss = []
		str = sys.argv[1]
		words = str.split()
		print(words)
		a = len(words)
		for word in words:
			if len(word) > int(sys.argv[2]):
				wordss.append(word)	
		print(wordss)
	else:
		print("ERROR")
else:
	print("ERROR")
