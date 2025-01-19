
"""
"""

def function(*args, **wargs):
	"""
	"""
	try:
		command = ["git", "fetch", "--tags"]
		import subprocess
		subprocess.run(command, capture_output=True, text=True, check=True).stdout
		command = ["git", "describe",
		           "--tags",
		           "`git rev-list --tags --max-count=1`"]
		import subprocess
		return subprocess.run(command, capture_output=True, text=True, check=True).stdout
	except subprocess.CalledProcessError as e:
		print(f"Error occurred: {e}")
		raise subprocess.CalledProcessError
