import requests
import urllib.request
import random
import pyautogui
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
from bs4 import BeautifulSoup
from selenium import webdriver

# 검색어
search = '셀스타그램'
#url
url = 'https://www.instagram.com/explore/tags/'+search+'/?hl=ko'

driver = webdriver.Chrome(executable_path='C:\\Users\\inaee\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(2) #브라우저 자체가 웹요소들을 기다리도록 만들어주는 옵션 /2초기다림
driver.get(url)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]').click()

f = open('C:\\Program Files\\Python35\\크롤러\\file.txt', 'a',encoding='utf8')

id=driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
ti=driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/div[1]/ul/li[1]/div/div/div/span').text
f.write(id)
f.write(' / ')
f.write(ti.translate(non_bmp_map))
f.write('\n\n')
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/a').click()
        
number=0 
while number<100:
    #아이디 ,내용 파일에 저장하기
    post=driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
    post2=driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/div[1]/ul/li[1]/div/div/div/span').text
    #이미지 저장하기
    #다음으로 넘어가기
    driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/a[2]').click()
    f.write(post)
    f.write(' / ')
    f.write(post2.translate(non_bmp_map))
    f.write('\n\n')
    number=number+1

f.close()
