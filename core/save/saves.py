"""
"""
def function(*args, **wargs):
	"""
	"""
	from save_raw import function as save_raw
	from save_last import function as save_last
	save_raw(*args)
	save_last(*args)