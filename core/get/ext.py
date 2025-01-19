
"""
"""

def function():
	"""
	"""
	ext = {'Windows': 'dll', 'Linux': 'so'}
	import platform; import os
	return ext[platform.system()]
