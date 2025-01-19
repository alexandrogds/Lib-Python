"""
"""
def function(*args, **wargs):
	"""
	"""
	if len(wargs) != 0: print('Pass uri by args'); raise NotImplemented
	from core.ls import get_paths_of_all_files_recursive_ls as ls
	from core.ls._process import get_all_files_and_folders_recursive_ls as xff
	return xff(ls(*args, **wargs))
