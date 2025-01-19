"""
"""
def function(*args, **wargs):
	"""
	"""
	from datetime import datetime
	d = str(datetime.utcnow()).replace(':', '..')
	import os
	path = os.path.join(os.environ['dirname'], f'../../../DataS/raw/{d}')
	path = os.path.abspath(path)
	import json
	with open(path, 'w') as f: f.write(json.dumps(args, indent=3))