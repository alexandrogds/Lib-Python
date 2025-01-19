
"""
"""

def f(*args, **wargs):
	if len(wargs) != 0: print('Pass uri by args'); raise NotImplemented
	if len(args) != 0: print('Pass uri by args'); raise NotImplemented
	import os
	folder = os.path.dirname(os.path.abspath(__file__))
	from core.path.recursive import get_last_dirfiles
	ff = get_last_dirfiles(folder)
	for k,v in ff:
		with open(v) as f:
			flag = 0
			folder = os.path.basename(k)
			content = f"""
	\"\"\"
	\"\"\"

	from core import Namespace

	class {folder}(Namespace):
		def __init__(*args, **wargs):
			pass    
	"""
			for line in f:
				if line[0:3] == 'def':
					flag = 1
					content = '\t' + line
				if flag and line[0] == '\t':
					content += '\t' + line