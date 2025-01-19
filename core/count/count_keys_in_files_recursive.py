
"""
"""

def function(*args, **wargs):
	"""
	wargs['project'], wargs['key']
	"""
	from core import map_wargs
	map_wargs(**wargs)
	from core import get_paths_of_files_recursive as paths
	paths = paths(project)
	count = 0
	for path in paths:
		with open(path) as f:
			for line in f:
				if line.strip().find(key) == 0:
					count += 1
	return count
