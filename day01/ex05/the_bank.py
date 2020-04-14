class Account(object):

	ID_COUNT = 1

	def __init__(self, name, *kwargs): # changement **kwargs
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(*kwargs) # kwargs
		val = self.__dict__['value'] # prob value
		if hasattr(self, 'value'): 
			self.value = val # self.value = 0
		Account.ID_COUNT += 1

	def transfer(self, amount):
		self.value += amount

class Bank(object):
	"""The bank"""
	def __init__(self):
		self.account = []

	def add(self, account):
		self.account.append(account)
		
	def transfer(self, origin, dest, amount):
		item_origin = None
		item_dest = None
		for item in self.account:
			if item.name == origin or item.id == origin:
				item_origin = item
			if item.name == dest or item.id == dest:
				item_dest = item
		if item_origin == None or item_dest == None or type(amount) is not float:
			return False
		if item_origin.value >= amount:
			item_origin.transfer(-amount)
			item_dest.transfer(amount)
		else:
			return False
#		print(item_origin.value)
#		print(item_dest.value)
#		print(item_origin.__dict__)
#		print(item_dest.__dict__)
	"""
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
	"""
	def get_item(self, account):
        	item_account = None
        	for item in self.account:
        		if item.name is account or item.id is account:
        			item_account = item
       		return item_account

	def fix_account(self, account):	
		print(self.get_item(account).__dict__)
		#dir fonction !!! account.dir(correction) ?? 
	"""
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
	"""
