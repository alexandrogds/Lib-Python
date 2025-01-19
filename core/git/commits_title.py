
"""
"""

def function(*args, **wargs):
	"""wargs[path, grep]"""
	from core import map_wargs
	map_wargs(**wargs)
	try:
		command = ["git", "log", f"--grep=\"{grep}\""]
		import subprocess
		return subprocess.run(command, capture_output=True, text=True, check=True, cwd=path).stdout
	except subprocess.CalledProcessError as e:
		print(f"Error occurred: {e}")
		raise subprocess.CalledProcessError
