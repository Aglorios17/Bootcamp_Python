import csv

class CsvReader():
	def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = None
		self.header_bool = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom

	def __enter__(self):
		self.fd = open(self.filename, 'r')
		return self

	def getheader(self):
		if self.header is None:
			self.header = self.fd.readline()
		return self.header

	def getdata(self):
		self.getheader()
		data = ""
		if (self.header_bool):
			data += self.fd.read()
		if self.skip_bottom is 0:
            		lst = self.fd.readlines()[self.skip_top:] # rend une liste de != chaine de charact [nombre:] passer le debut
		else:
			lst = self.fd.readlines()[self.skip_top:-self.skip_bottom] # :- = enlever ...
		for s in lst:
			data += s
		return data
		
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.fd.close()

if( __name__ == "__main__" ):
	with CsvReader('good.csv') as file:
		data = file.getdata()
		print (data)
		print ('\n')
		header = file.getheader()
		print (header)
