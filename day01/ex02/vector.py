class Vector:
	def __init__(self, data):
		if type(data) is list:
			self.values = data
			self.size = len(self.values)
		elif type(data) is int:
			i = 0.0
			vector = []
			while i < data:
				vecteur.append(i)
				i += 4
			self.values = vector
			self.size = data
		elif type(data) is tuple and len(data) == 2:
			x = float(data[0])
			vector = []
			while x < data[1]:
				vector.append(x)
			self.values = vector
			self.size = len(vector)
		else:
			print("error")

