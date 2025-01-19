"""
cp -r ~/public_html_bk_parcial/* ~/public_html
# para reverter
"""
root="/home/alexandrogonsan/"
#root="/home1/rrcom860/"
report="2021-06-10 16.00.21 public_html e.md"
sistema="public_html/"

import os
import shutil
import time

# sair=False
# with open(root+"php7mar/reports/"+report) as f:
# 	for line in f:
# 		if line.strip().find("* Line")!=0:
# 			variableInterpolation=False
# 			newOperatorWithReference=False
# 			oldClassConstructors=False
# 		if line.find("#### ")==0:
# 			file=line[5:-1]
# 		elif line.strip()=="* variableInterpolation":
# 			variableInterpolation=True
# 		elif variableInterpolation:
# 			line=line.strip().split('`')[1].strip()
# 			with open(file) as g:
# 				count_lines=0
# 				for l in g:
# 					if l.strip()==line:
# 						count_lines+=1
# 				if count_lines!=1:
# 					print file
# 					print line
# 					print count_lines
# 					sair=True
# 		elif line.strip()=="* newOperatorWithReference":
# 			newOperatorWithReference=True
# 		elif newOperatorWithReference:
# 			line=line.strip().split('`')[1].strip()
# 			with open(file) as g:
# 				count_lines=0
# 				for l in g:
# 					if l.strip()==line:
# 						count_lines+=1
# 				if count_lines!=1:
# 					print file
# 					print line
# 					print count_lines
# 					sair=True
# 		elif line.strip()=="* oldClassConstructors":
# 			oldClassConstructors=True
# 		elif oldClassConstructors:
# 			line=line.strip().split('`')[1].strip()
# 			with open(file) as g:
# 				count_lines=0
# 				for l in g:
# 					if l.strip()==line:
# 						count_lines+=1
# 				if count_lines!=1:
# 					print file
# 					print line
# 					print count_lines
# 					sair=True
# if sair==True:
# 	print 'fail'
# 	exit()
with open(root+"php7mar/reports/"+report) as f:
	line_number=0
	for line in f:
		line_number+=1
		if line.strip().find("* Line")!=0:
			variableInterpolation=False
			oldClassConstructors=False
			newOperatorWithReference=False
		if line.find("#### ")==0:
			file=line[5:-1]
			file_backup=file.replace("public_html","public_html_bk_parcial")
			pasta='/'.join(file_backup.split('/')[:-1])+'/'
			try:
				os.makedirs(pasta)
			except:
				None
			shutil.copyfile(file, file_backup)
			scripts=["comment_out_getset_magic_quotes_runtime.sh",
				"mysql_to_mysqli.sh",
				"ereg_replace_to_preg_replace.sh",
				"short_to_long_open_tag.sh",
				"ereg_to_preg_match.sh",
				"split_to_preg_split.sh",
				"mysql_real_escape_string_to_mysqli.sh",
				"while_each_to_foreach.sh"]
			for script in scripts:
				os.system("bash "+root+"php-migration/scripts/src/"+script+" \""+file+"\"")
		elif line.strip()=="* variableInterpolation":
			variableInterpolation=True
		elif variableInterpolation:
			line=line.strip().split('`')[1].strip()
			content=None
			with open(file) as g:
				content=g.read()
			g=content.split('\n')
			for i in range(len(g)):
				if g[i].strip()==line:
					aux=g[i].split('::')
					aux2=None
					if len(aux)==2:
						aux[1]='{'+aux[1].replace(']',"]}")
						g[i]='::'.join(aux)
						# break
					elif len(aux)==1:
						aux2=aux[0].split('->')
						fim=False
						for a in range(len(aux2)):
							if aux2[a].find(']')!=-1:
								if aux2[a].count(']')>1:
									print 'error multiples ]'
									print file
									print g[i]
									fim=True
									exit()
								aux2[a]='{'+aux2[a].replace(']',"]}")
						aux2='->'.join(aux2)
						g[i]=aux2
					else:
						print 'error multiple :: for line'
						print file
						print g[i]
						exit()
					# break
			g='\n'.join(g)
			with open(file,'w') as h:
				h.write(g)
		elif line.strip()=="* newOperatorWithReference":
			newOperatorWithReference=True
		elif newOperatorWithReference:
			line=line.strip().split('`')[1].strip()
			content=None
			with open(file) as g:
				content=g.read()
			g=content.split('\n')
			for i in range(len(g)):
				if g[i].strip()==line:
					if g[i].count('=&')!=1:
						print 'error multiples =&'
						print file
						print g[i]
						break
					aux=g[i].split('=&')
					timestamp=str(time.time()).split('.')[0]
					spaces=''
					for c in g[i]:
						if c=='\t':
							spaces+=c
						elif c==' ':
							spaces+=c
						else:
							break
					if line.find('//')==0:
						start_line=spaces+"// $instance_20210531_"
					else:
						start_line=spaces+"$instance_20210531_"
					g[i]=start_line+timestamp+" ="+aux[1]+\
						'\n'+aux[0]+'=& $instance_20210531_'+timestamp+';'
					# break
			g='\n'.join(g)
			with open(file,'w') as h:
				h.write(g)
		elif line.strip()=="* oldClassConstructors":
			oldClassConstructors=True
		elif oldClassConstructors:
			line=line.strip().split('`')[1].strip()
			content=None
			with open(file) as g:
				content=g.read()
			g=content.split('\n')
			for i in range(len(g)):
				if g[i].strip()==line:
					aux=g[i].split('(')
					aux2=aux[0].split(' ')
					aux2[-1]="__construct"
					aux2=' '.join(aux2)
					aux[0]=aux2
					aux='('.join(aux)
					g[i]=aux
					# break
			g='\n'.join(g)
			with open(file,'w') as h:
				h.write(g)
		else:
			None