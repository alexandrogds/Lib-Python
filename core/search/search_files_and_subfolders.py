"""
"""
def function(*args, **wargs):
	"""
	"""
	r = []
	for path in wargs['files']:
		import os
		file = os.path.basename(path)
		for search in wargs['searchs']:
			if search.lower() in file.lower():
				if os.path.isfile(path):
					r += [path]
				else:
					from get_all_subfiles import function as get_all_subfiles
					r += get_all_subfiles(path)
	return r