"""
"""
def function(*args, **wargs):
	"""
	"""
	from get_paths_relative_of_files_recursive import function as get_paths_relative_of_files_recursive
	_0xff = get_paths_relative_of_files_recursive(wargs['components'])
	from convert_paths_to_case_sensitive_names import function as convert_paths_to_case_sensitive_names
	components = convert_paths_to_case_sensitive_names(_0xff)
	import subprocess; import os
	if wargs['project'] == None:
		_ = wargs['components'].find('resources/views')
		wargs['project'] = wargs['components'][:_]
	for i in range(len(components)):
		components[i] = components[i][:-10]
		if components[i].find('Components') == 0:
			components[i] = components[i].replace('Components', '')
		if components[i] == '':
			continue
		command = ['php', 'artisan', 'make:component', components[i]]
		subprocess.run(command, cwd=wargs['project'])
		components[i] = os.path.join(wargs['project'], 'app/View/Components', components[i] + '.php')
		from get_name_of_import_blade_laravel import function as get_name_of_import_blade_laravel
		_ = get_name_of_import_blade_laravel(_0xff[i])
		#script = f"s|return view('/c\\return view('bootstrap.{_}')|"
		#command = ['sed', '-i', script, components[i]]
		#subprocess.run(command)
		with open(components[i]) as f:
			c = ''
			for line in f:
				if line.find("return view('") != -1:
					c += f"\t\t\treturn view('bootstrap.{_}');\n"
				else:
					c += line
		with open(components[i], 'w') as f: f.write(c)