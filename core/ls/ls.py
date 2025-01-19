
"""
"""

def function(*args, **wargs):
	"""
	"""
	try:
		command = ["ls"] + args
		import subprocess
		return subprocess.run(command, capture_output=True, text=True, check=True).stdout
	except subprocess.CalledProcessError as e:
		print(f"Error occurred: {e}")
		raise subprocess.CalledProcessError
	except FileNotFoundError:
		print("ls command not found. Make sure it's installed or use find + grep instead.")
		raise FileNotFoundError
