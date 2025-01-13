import openpyxl
from konlpy.tag import Twitter
from konlpy.utils import pprint

wb=openpyxl.load_workbook('C:\\Program Files\\Python35\\크롤러\\insta.xlsx')
ws=wb.active

#"Twitter"has changed to "Okt" since KoNLPy v0.4.5
twitter=Twitter()

for r in ws.rows:
    row_index=r[0].row
    xx=r[2].value

    #print(xx)
    yy=twitter.pos(xx)
    #print(yy)

    #sentences=xx.jki.morphAnalyzer(phrase)
    #morphemes=[]
    #if not sentences:
    #    morphemes
    
    b=""
    for j in range(0,int(len(yy))):
        b=b+yy[j][0]+""+yy[j][1]+" / "
    print(b)
    ws.cell(row=row_index, column=6).value=b


wb.save('C:\\Program Files\\Python35\\크롤러\\insta.xlsx')
wb.close()
