#id당 게시물 10개 각 폴더에 저장하기

import openpyxl
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import sys


i='_.mi_la_'
url='https://www.instagram.com/'+i+'/?hl=ko'

driver = webdriver.Chrome(executable_path='C:\\Users\\inaee\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(2) 
driver.get(url)

#driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a').click()

count = 0
img = driver.find_elements_by_tag_name("img")

for item in img:
    if (count > 0 and count < 11):
        full_name = "C:\\Program Files\\Python35\\크롤러\\_.mi_la_\\" + str(count) + ".jpg"
        try:
            urllib.request.urlretrieve(item.get_attribute('src'), full_name)
        except:
            urllib.request.urlretrieve(item.get_attribute('data-src'), full_name)
    count = count+1
    
driver.Quit()
