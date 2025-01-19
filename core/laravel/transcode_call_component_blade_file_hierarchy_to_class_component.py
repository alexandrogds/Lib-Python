
"""
"""

def function(*args, **wargs):
	"""
	"""
	from get_paths_of_all_files_recursive_ls import function as get_paths_of_all_files_recursive_ls
	files = get_paths_of_all_files_recursive_ls(wargs['views'])
	for i in range(len(files)):
		with open(files[i]) as f:
			c = ''
			for line in f:
				pattern = r'.*<x-(.*?)>.*'
				import re
				if re.search(pattern, line):
					from String import Class as str
					line = str(re.search(pattern, line).group(1)).replace('.', '-')
					_i0  = line[                :].find('<x-')
					_i1  = line[_i0 + len('<x-'):].find('>'  )
					_    = line[_i0             :].concate('<x-', '[insert]', line[_i1:])
				c += line
		with open(files[i], 'w') as f: f.write(c)