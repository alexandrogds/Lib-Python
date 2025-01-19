
"""
"""

class Class(str):
	"""
	"""

	def __init__(self, value):
		"""
		"""
		self.value = str(value)

	def concatenate(self, *args):
		"""
		"""
		for arg in args:
			self.string += str(arg)
	concat = concatenate
	concate = concatenate

	def __str__(self):
		"""
		"""
		return self.value
	
	def __getitem__(self, index):
		"""
		"""
		return Class(self.value[index])

if __name__ == '__main__':
	print(Class('asd') + Class('asd'))