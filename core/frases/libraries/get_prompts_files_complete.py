def f():
	import os
	a85=[]
	for a91 in os.scandir():
		if True \
				and a91.is_file() \
				and a91.path.find('_')!=-1 \
				:
			a88='/'.join(__file__.split('/')[:-1])
			a85.append(a88+'/'+a91.path.split('/')[1])
	return a85