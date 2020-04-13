import sys
def whois(str):
	i = len(sys.argv)
	if i != 2 or sys.argv[1].isnumeric() is False:
		print ("ERROR")
		return 0
	i = int(sys.argv[1])
	if i == 0:
		print("I'm Zero.")
	elif i % 2 == 0:
		print("I'm Even.")
	elif i % 2 != 0:
		print("I'm Odd.")
whois(sys.argv)
