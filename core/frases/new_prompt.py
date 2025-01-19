import os
fullpath=__file__.split('/')[:-1]
model=fullpath+'/model_prompt'
prompt=f''
cmd=f'cp {model} {prompt}'
os.system(cmd)
os.system('cp first $(date +"%s")')