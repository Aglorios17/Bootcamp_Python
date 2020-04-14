class Evaluator:
	def enumerate_evaluate(coefs, words):
		if len(coefs) is not len(words):
#			print('\n')
			return -1
		else:
			return sum([coefs[i] * len(w) for i, w in enumerate(words)])
	def zip_evaluate(coefs, words):
		if len(coefs) is not len(words):
#			print('\n')
			return -1
		else:
			return sum([c * len(w) for c, w in zip(coefs, words)])
			
