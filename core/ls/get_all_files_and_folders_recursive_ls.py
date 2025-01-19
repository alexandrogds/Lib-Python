"""
"""
def function(*args, **wargs):
	"""
	"""
	from core import ls_recursive_of_files_python as ls
	_ = ls(*args, **wargs)
	from core import process_gets_files_and_foldes_of_ls_command as process
	return process(_)