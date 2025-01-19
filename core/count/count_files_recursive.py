
"""
"""

def function(*args, **wargs):
	"""
	"""
	from core import ls
	_ = ls('-la', '--ignore=.git', str(args[0]))
	_ = _[6:]
	r = ''
	for c in _:
		if c != '\n':
			r += c
	return int(r)