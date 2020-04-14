from time import time

def generator(text, sep=' ', option=None):
	lst_option = ["shuffle", "unique", "ordered", None]
	txt = []
	if type(text) is not str or option not in lst_option:
		return "ERROR"
	lst_txt = text.split()
	if option == "ordered":
		lst_txt.sort(key=lambda x:(not x.islower(), x))
	elif option == "unique":
		lst_txt = sorted(set(lst_txt))
	elif option == "shuffle":
		while len(lst_txt) > 0:
         		txt.append(lst_txt.pop(int(time()) % len(lst_txt) - 1))
		lst_txt = txt
	elif option == None:
		return None
	return lst_txt
