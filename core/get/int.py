
"""
"""

def function():
	"""
	"""
	import os
	LibS = os.path.abspath(os.path.join(os.path.dirname(__file__), "../LibS/"))
	import ctypes; from get_ext_lib import function as get_ext_lib
	ext = get_ext_lib(); filename = f'int.{ext}'
	return ctypes.cdll.LoadLibrary(os.path.join(LibS, filename)).max()
