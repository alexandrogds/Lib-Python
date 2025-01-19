import time
import os
import selenium
import qrcode
import PIL
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.set_headless(True)
driver = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe')
driver.get('http://web.whatsapp.com')
driver.set_window_size(1400,900)
time.sleep(1)

token = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div').get_attribute('data-ref')
img = qrcode.make(token)
size = 300,300
img.thumbnail(size, PIL.Image.ANTIALIAS)
img.show()
time.sleep(6)
img.close()