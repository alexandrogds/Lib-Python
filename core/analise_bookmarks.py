#!/usr/bin/python3

import argparse

def a93():
	a99="/home/alexandrogonsan/favoritos_20_06_2021.html"
	a96=None
	with open(a99) as a98:
		a97=a98.read()
		a96=a97.split('\n')
		line=54
		# a96[line-1]=a96[line-1].replace('DL','DT')
		# a96[line-1]='                        <DT><A HREF="https://www.bing.com/search?q=Could+not+find+method+implementation%28%29+for+arguments+%5Bcom.google.android.gms%3Aplay-services-instantapps%3A17.0.0%5D+on+project&go=Pesquisar&qs=ds&form=QBRE" ADD_DATE="1621364975" ICON="">Could not find method implementation for arguments com google android gms play services instantapps 17 0 0 on project   Bing</A>'
		# a92=a96.count('                        <DT><A HREF="https://www.bing.com/search?q=Could+not+find+method+implementation%28%29+for+arguments+%5Bcom.google.android.gms%3Aplay-services-instantapps%3A17.0.0%5D+on+project&go=Pesquisar&qs=ds&form=QBRE" ADD_DATE="1621364975" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACXklEQVQ4jZWTT0hUURjFz3ffn3FGZ9RMTamFBS00KIgiKAIhCIqCiBGCCIKoXbtatchq61JI2gS1GmmR4MrAIGghriKpaJOZ6YzMvHHmvZl377vvfi1egxoV9e0ul/Pju+ecCwAAMwHAiXn/zKk34U38xwgAwDgIAIQW15yO1NTJuebs8dnawX8H3AcDAEtS2oOx3LZzFpwXR6fY+VcAAQCUII5AUVnGrMSQvQ/p5J5F65m/B/wcEwEsQaxgsYTWK9AJgAyIGAW2fgXYO04hCARAEgBiD55z7BUXWJiKIvno3Sh9+/sGIYElwFKAQxJBrVuDeI/dJ24Zx1oYWgjuYWnJ/SOAA4bxGSYw4CZbxTsURLZ5LBtgTbo36sk87Ned08OFLUjLxGSDIILxAeNrmHoc781zeq3LeimbzZLqzdhhsxT1dLVf7B5x8wCAQsFKAJzEaOoG8SbB1GOYumZ3v+cWD6MRdcSjflyfcCrK2+XA5FJ0GgCQz3NiYmIdaz82SBk2UoMJVC/pGCDun15e72RLllZVh3ekiv7LKtGNb6XAAKB9mTahBLOmWBqz8Ql8dqZ6Qxb5gbOZGWj3ypH8aAmzHrwHAAxP044i5QZRiaoN+F/9yLYiXJjIzrlu+xNLYIBUXWa6dzspJ14OV9RzAMDYWJy0i5lAxFc+80h50V/UfiyyB9qMSFltsugrVRWurmXhr27OBI3m7Q+Tg8utFLbq2YJ856sUYTJuIKdrgPIMwrXgS7CB8bd3c0+36XgnYBvk/Lw8lMral0yItCoHXqMSPnt9vW8daP0H4pbkB1H4QbCB//9FAAAAAElFTkSuQmCC">Could not find method implementation for arguments com.google.android.gms play-services-instantapps 17.0.0 on project - Bing</A>')
		# print(a92)
		print(a96[line-1])
		# exit()
		if True:
		# if input('remove?') in ['Y','y']:
			a96.remove(a96[line-1])
			
		a95='\n'.join(a96)
	import os
	a94=f'cp "/home/alexandrogonsan/favoritos_20_06_2021.html" "/home/alexandrogonsan/favoritos_20_06_2021_line_{line}_$(date +"%s").html"'
	os.system(a94)
	with open(a99,'w') as a98:
		a98.write(a95)
	a94=f'cp "/home/alexandrogonsan/favoritos_20_06_2021.html" "/home/alexandrogonsan/Área de trabalho/favoritos_20_06_2021.html"'
	os.system(a94)
a93()
def a92():
	from xml.dom.minidom import parse
	import xml.dom.minidom
	# Open XML document using minidom parser
	try:
		DOMTree = xml.dom.minidom.parse(a99)
		None
	except:
		a96=None
		with open(a99) as a98:
			a97=a98.read()
			a96=a97.split('\n')
			line=55
			print(a96[line-1])
		import traceback
		traceback.print_exc()
class a89(argparse.Namespace):
	def __init__(self):
		import xml.etree.ElementTree as ETree
		
	def a91(self):
		tree = ETree.fromstring("C:/Users/XXX/Downloads/test_xml.xml", parser=parser)
		a91_(tree)
	def a91_2(self):
		tree = ETree.parse(a99, parser=parser)
		a91_(tree)
	def a91_(sekf,tree):
		parser = ETree.XMLParser(encoding="utf-8")
		try:
			print(ETree.tostring(tree.getroot()))
		except:
			import traceback
			traceback.print_exc()
a91=a89().a91
a91_2=a89().a91_2
def a90():
	pass

a99="/home/alexandrogonsan/favoritos_20_06_2021.html"
# a92()
# a91()
a91_2()