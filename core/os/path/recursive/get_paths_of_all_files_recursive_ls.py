
"""
"""

def function(*args, **wargs):
	"""
	"""
	from core import ls_recursive_of_files_python as ls
	_ = ls(*args, **wargs)
	from core import process_get_paths_of_files_of_ls_command as proccess
	return process(_)
