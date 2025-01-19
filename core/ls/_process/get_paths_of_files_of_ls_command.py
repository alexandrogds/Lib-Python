"""
"""
def function(*args, **wargs):
	"""
	"""
	folder = None
	r = []
	for line in args[0].split('\n'):
		if line.strip() == '':
			continue
		import os
		if line[0] == '/':
			folder = line
		elif os.path.isfile(os.path.join(folder[:-1], line[:])):
			r += [os.path.join(folder[:-1], line[:])]
	return r