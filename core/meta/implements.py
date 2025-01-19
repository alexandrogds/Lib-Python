
"""
"""

def f(*args, **wargs):
	"""
	"""
	all, contents = args
	if len(wargs) != 0: print('Pass uri by args'); raise NotImplemented
	for i in range(len(all)):
		for term in all[i]:
			import os
			diretorio = os.path.dirname(os.path.join(term))
			if not os.path.exists(diretorio):
				os.makedirs(diretorio)
			with open(term, 'w') as arquivo:
				arquivo.write(contents[i])