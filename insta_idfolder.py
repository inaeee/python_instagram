#엑셀에 저장한 id로 된 폴더생성

import openpyxl
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import urllib.request
import os

#엑셀 파일열기
wb = openpyxl.load_workbook('C:\\Program Files\\Python35\\크롤러\\insta.xlsx')
print (type(wb))
#현재 active sheet 얻기
ws=wb.active

ids=[]
for row in ws.iter_rows(min_row=2, min_col=2, max_col=2):
    id=[]
    for cell in row:
        id.append(cell.value)
    ids.append(id)
idsAll=sum(ids,[])
print (idsAll)

#id로 된 폴더생성
count=1
for i in idsAll:
    def make_foler(i):
        if not os.path.isdir(i):
            os.makedirs(i)
    work_dir='C:\\Program Files\\Python35\\크롤러\\'+str(i)+'\\'
    make_foler(work_dir)
    count+=1
