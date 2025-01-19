
"""
"""

def function(*args, **wargs):
	"""
	"""
	for k, v in wargs.items():
		try:
			__builtins__[k] = v
		except:
			setattr(__builtins__, k, v)