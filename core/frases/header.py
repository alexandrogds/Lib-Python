
# modules to use in this file
import importlib
import inspect
import sys
import importlib.util
from importlib import import_module


# packages of python3 and not modules of python
# it are in folder diff

# import argparse
# import a


# setattr(__builtins__,'importlib',importlib)
# setattr(__builtins__,'import_module',getattr(importlib, 'import_module'))
# Function get_method_from_file com base abaixo de mesmo nome.
# https://www.it-swarm.dev/pt/python/importar-dinamicamente-um-metodo-em-um-arquivo-de-uma-string/940873083/

# def get_method_from_file(full_path):
# 	if len(full_path) == 1:
# 		__builtins__[full_path[0].split('.')[-1]] = \
# 			import_module(full_path[0])
# 		return __builtins__[full_path[0].split('.')[-1]]
# 	module = get_method_from_file(full_path[:-1])
# 	if module != None:
# 		__builtins__[full_path[0].split('.')[-1]] = \
# 			getattr(module,full_path[-1])

# modules = [
	# ('sys'),
	# #('os'),
	# ('ctypes'),
	# ('inspect'), ('itertools'), ('re'), ('string'),
	# ('subprocess'),  ('time'),('importlib'),('requests'),

	# ('importlib.machinery'),

	# ('bs4','BeautifulSoup'),
	# ('itertools','product'),
	# ('datetime','datetime.now'), ('datetime','datetime.utcnow'),
	# ('os','environ'), ('os','fork'), ('os','listdir'),
	# ('os','path'), ('os','system'), ('os.path','exists'),
	# ('os.path','isfile'), ('os.path','islink'), ('os.path','join'),
	# ('re','findall'), ('sys','argv'), ('subprocess','call'),
	# ('time','sleep'),

	# ('a'),

	# ('argparse')
	# ]

# def i(name):
# 	# try:
# 		for name, obj in inspect.getmembers(sys.modules[name]):
# 			# if inspect.isclass(obj):
# 			# print(name)
# 			try:
# 				# setattr(__builtins__,name,eval(module+'.'+name))
# 				__builtins__[name] = eval(module+'.'+name)
# 			except:
# 				None
# 			#print('import sucess')
# 			if inspect.ismodule(name):
# 				print('is submodule =',name)
# 				i(name)
# 	# except:
# 	#     print('error = error')
# 	#     None

modules=[]
from libraries import full_path as full_path_
a99=[('path','full'),('path','project')]
for a98 in a99:
	import itertools
	a97=itertools.permutations(a98, 2)
	for a96 in a97:
		__builtins__['_'.join(a96)]=full_path_.f(__file__)
		__builtins__[''.join(a96)]=full_path_.f(__file__)
from libraries import get_subdirs_root as a94
a99=[('get','dirs','root'),('get','subdirs','root'),
	('get','subdir','root'),('get','dir','root')]
for a98 in a99:
	import itertools
	a97=itertools.permutations(a98, 2)
	for a96 in a97:
		__builtins__['_'.join(a96)]=a94.f(__file__)
		__builtins__[''.join(a96)]=a94.f(__file__)

import importlib.util

a97='/home/alexandrogonsan/frases/libraries/get_option.py'
MODULE_PATH = a97
MODULE_NAME = a97.split('/')[-1].split('.')[0]
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
get_option1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(get_option1)
__builtins__[MODULE_NAME] = get_option1
get_option.f('ok')

import os
with open(os.path.join(fullpath,'libraries')) as a95:
	None

for module in modules:
	if type(module) == str:
	# if type(module) == type(tuple):
		# print('module =',module)
		try:
			__builtins__[module] = import_module(module)
			# setattr(__builtins__,module,import_module(module))
		except:
			print('module import error =',module)
			None
		i(module)
	# elif len(module) == 2:
	#     print('ok')
	#     exit()
	#     #get_method_from_file((module[0]+'.'+module[1]).split('.'))
	#     __builtins__[module[1].split('.')[-1]] = \
	#         import_module(module[0],package=module[1])
	#     __builtins__[module[1].split('.')[-1]] = \
	#         eval(module[1].split('.')[-1]+'.'+module[1])
	# else:
	#     print('ERROR: MODULE_IMPORT_WITHOUT_RECOMENDATION')
# def start(file):
	# setattr(file,'os',import_module('os'))
None
