
"""
"""

def function(*args, **wargs):
	"""
	"""
	from core import ls
	return ls("-laRABx1", "--ignore=node_modules",
						"--ignore=.git", "--ignore=assets",
						"--ignore=output", "--ignore=*.so",
						"--ignore=*.dll", "--ignore=*.pyc",
						str(args[0]))
