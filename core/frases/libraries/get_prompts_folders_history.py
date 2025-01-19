def f():
	import os
	a89=[]
	for a91 in os.scandir():
		if True \
				and a91.is_dir() \
				and a91.path.find('./.')==-1 \
				and a91.path.find('./prompt')==-1 \
				:
			a88='/'.join(__file__.split('/')[:-1])
			a89.append(a88+'/'+a1.path.split('/')[1])
			print(f'0={a91.path}')
	return a89
if __name__=='__main__':
	print(f())