import importlib
import os
print('ab'.replace('a','b'))
print(os.getcwd())
print(__file__)
print(['']*3)
a99=open('index.py')
with a99 as a98:
	print(a98.read()[:100])
def get_method_from_file(full_path):
	from importlib import import_module
	if len(full_path) == 1:
		__builtins__[full_path[0].split('.')[-1]] = \
			import_module(full_path[0])
		return __builtins__[full_path[0].split('.')[-1]]
	module = get_method_from_file(full_path[:-1])
	if module != None:
		__builtins__[full_path[0].split('.')[-1]] = \
			getattr(module,full_path[-1])

import importlib.util
a97='/home/alexandrogonsan/frases/libraries/get_option.py'
MODULE_PATH = a97
MODULE_NAME = a97.split('/')[-1].split('.')[0]
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
get_option1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(get_option1)
def add_module(MODULE_NAME,module):
	if module.
	try:
		__builtins__[MODULE_NAME] = get_option1
	except:
		setattr(__builtins__,MODULE_NAME,get_option1)
# get_option.f('ok?')

a96=[1,2,3]
a96.remove(1)
print(a96)