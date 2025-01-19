
"""
"""

def f(*args, **wargs):
	if len(wargs) != 0: print('Pass uri by args'); raise NotImplemented
	aux = ''
	for c in args:
		parts = []
		if c in ['/', '\\']:
			parts += [aux]
			aux = ''
		else:
			aux += c
	return parts