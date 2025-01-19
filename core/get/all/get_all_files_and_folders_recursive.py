"""
"""
def function(*args, **wargs):
	"""
	"""
	import os
	r = []
	for root, subfolders, files in os.walk(args[0]):
		for file in files:
			if file.split('.')[-1] in ['so', 'dll', 'pyc']:
				continue
			elif file == 'output':
				continue
			file_path = os.path.join(root, file)
			r += [file_path]
		for subfolder in subfolders:
			if subfolder in ['node_modules', '.git', 'assets', 'DataS']:
				continue
			folder_path = os.path.join(root, subfolder)
			r += function(subfolder)
	return r