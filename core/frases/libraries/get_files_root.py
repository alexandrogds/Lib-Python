def f(root):
	import os
	a85=[]
	for a91 in os.scandir(root):
		if True \
				and a91.is_file() \
				:
			a83=a91.path.split('/')[1]
			a84=os.path.join(root,a83)
			a85.append(a84)
	return a85