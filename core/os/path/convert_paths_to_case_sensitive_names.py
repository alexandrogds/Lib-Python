"""
"""
def convert_paths_to_case_sensitive_names(*args, **wargs):
	"""
	"""
	names = []
	for path in args[0]:
		_ = path.replace('/', ' ').replace('-', ' ')
		_ = _.title().replace(' ', '')
		names += [_]
	return names