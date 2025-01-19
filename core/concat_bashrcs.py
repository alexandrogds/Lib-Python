with open("/home/alexandrogonsan/find_bashrcs") as a9:
	a6=''
	for a8 in a9:
		if a8.find('#')!=0:
			with open(a8.strip().replace('./','/home/alexandrogonsan/')) as a7:
				a6+=a7.read()
				a6+='\n'
	with open('/home/alexandrogonsan/bashrcs_concat','w') as a5:
		a5.write(a6)