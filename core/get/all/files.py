
"""
"""

def f(directory):
	"""
	"""
	all_subfiles = []
	import os
	for root, subfolders, files in os.walk(directory):
		for file in files:
			file_path = os.path.join(root, file)
			all_subfiles += [file_path]
		for subfolder in subfolders:
			all_subfiles += function(os.path.join(root, subfolder))
	return all_subfiles

if __name__ == '__main__':
	function('c:/')
