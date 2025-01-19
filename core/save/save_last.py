
"""
"""

def save(*args, **wargs):
	"""
	"""
	EOL = '\n'
	for path, c in args:
		for i in range(len(path)):
			o = ''
			import os
			o += '//# FILE: '
			o += str(path[i])
			p = os.path.join(os.environ['dirname'], 'output', str(i))
			o += EOL
			o += str(c[i])
			with open(p, 'w') as f: f.write(o)

def function(*args, **wargs):
	"""
	"""
	from datetime import datetime
	datetime.utcnow()
	import os
	save(*args)
	