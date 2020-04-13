import sys

def error(str):
	i = len(sys.argv)
	if i < 3:
		print("Usage:  python operations.py <number1> <number2>")
		print("Example:")
		print("	   python operations.py 10 3")
		return 1
	elif i > 3:
		print("InputError: too many argument", end='\n''\n')
		print("Usage:  python operations.py <number1> <number2>")
		print("Example:")
		print("	   python operations.py 10 3")
		return 1
	elif sys.argv[1].isdigit() is False or sys.argv[2].isdigit() is False:
		print("InputError: only numbers", end='\n''\n')
		print("Usage:  python operations.py <number1> <number2>")
		print("Example:")
		print("	   python operations.py 10 3")
		return 1
def ope(str):
	if error(str) == 1:
		a = 0;
	else:	
		a = int(sys.argv[1])
		b = int(sys.argv[2])
		c = a + b
		print("Sum:	    ",c)
		c = a - b
		print("Difference: ",c)
		c = a * b
		print("Product:    ",c)
		if b == 0:
			print("Quotient:    ERROR (div by zero)")
			print("Remainder:   ERROR (module by zero)")	
		else:
			c = float(a) / float(b)
			print("Quotient:   ",c)
			c = a % b
			print("Remainder:  ",c)	
ope(sys.argv)
