import sys

def revers(str):
	return str[::-1].swapcase()
i = 0
i = len(sys.argv)

while i > 1:
	i -= 1
	if i != 1: 
		print(revers(sys.argv[i]), end= ' ')
	else:
		print(revers(sys.argv[i]))
