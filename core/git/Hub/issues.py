
"""
"""

def function(*args, **wargs):
	"""wargs[path, label, status]"""
	from core import map_wargs
	map_wargs(**wargs)
	try:
		command = [f"gh", "issue", "list",
	              "--state", status, "--label",
		            f"\"{label}\""]
		import subprocess
		return subprocess.run(command, capture_output=True, text=True, check=True, cwd=path).stdout
	except subprocess.CalledProcessError as e:
		print(f"Error occurred: {e}")
		raise subprocess.CalledProcessError
