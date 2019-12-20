import requests
import urllib.request
import random
from bs4 import BeautifulSoup
from selenium import webdriver

# id
id = 'r_____im__01'
# url
url = 'https://www.instagram.com/'+id+'/?hl=ko'

driver = webdriver.Chrome(executable_path='C:\\Users\\inaee\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get(url)

img = driver.find_elements_by_tag_name("img")

for item in img:
    full_name = "C:\\Program Files\\Python35\\크롤러\\사진\\" + id + ".jpg"
    try:
        urllib.request.urlretrieve(item.get_attribute('src'), full_name)
        print(item.get_attribute('src')[:30] + " : ")
    except:
        urllib.request.urlretrieve(item.get_attribute('data-src'), full_name)
        print(item.get_attribute('data-src')[:30] + " : ")
    print("{0}. Saving : {1}".format(count,full_name))
    
driver.Quit()

print("Saved!")
