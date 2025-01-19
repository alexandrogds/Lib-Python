import os
# import get_option as get_option
from libraries import get_prompts_folders_history as get_prompts_folders_history, get_prompts_files_complete as get_prompts_files_complete

a85=get_prompts_files_complete.f()
a84=get_prompts_folders_history.f()
a89,a96,a97=a84,None,['']*len(a85)
# a87=get_option.f('Qual prompt usar?')
with open(f'{a89[a87]}/id') as a94: a96=int(a94.read())
while True:
	for a83 in range(len(a85)):
		with open(a85[a83]) as a95:
			a98=f.read()
			if a98.find(a97) != -1:
				a97[a83]=a98.replace(a97[a83],'')
				os.system('mkdir '+a89[a87]+'/')
				a84=f'{a89[a87]}/get_return_{id}'
				a98=open(a84, 'w')
				with a98 as a92: a92.write(a97[a83])
				a83=open(f'{a89[a87]}/id','w')
				with a83 as a86: a86.write(str(id+1))