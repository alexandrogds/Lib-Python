import os
import glob
for pack in os.walk('/'):
	for f in pack[2]:
		fullpath = pack[0] + "/" + f
		# print(fullpath)
		if True \
				and fullpath.find('/proc')!=0 \
				and fullpath.find('/media')!=0 \
				and fullpath.find('/dev')!=0 \
				and fullpath.find('/boot')!=0 \
				:
				# and fullpath.find('/home')!=0 \
				# and fullpath.find('/dev')!=0 \
				# and fullpath.find('/run')!=0 \
				# and fullpath.find('/sys')!=0 \
				# and fullpath.find('/tmp')!=0 \
			cmd="cd / && sudo git add "+fullpath
			# print(cmd)
			os.system(cmd)
