import os
with open("/media/alexandrogonsan/c000cdb8-8663-4db7-a953-ab42e68203e1/home/alexandrogonsan/20210617/bash_history") as f:
	for l in f:
		if l.find("sudo apt install")==0 \
				or l.find("sudo apt-get install")==0:
			if l.find('')!=-1:
				# searched
				## screen
				## recorder
				## not show, find by apt search screenrecorder=simplescreenrecorder
				app='install'.join(map(str.strip,l.split('install')[1:]))
				print(app)