with open("/home/alexandrogonsan/sudo_find_bash_historys") as a9:
	a6=''
	for a8 in a9:
		if a8.find('#')!=0:
			with open(a8.strip().replace('./','/')) as a7:
				a6+=a7.read()
				a6+='\n'
	with open('/home/alexandrogonsan/bash_historys_concat','w') as a5:
		a5.write(a6)