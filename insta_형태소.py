import openpyxl
from konlpy.tag import Kkma

wb=openpyxl.load_workbook('C:\\Program Files\\Python35\\크롤러\\insta.xlsx')
ws=wb.active

kkma=Kkma()

for r in ws.rows:
    row_index=r[0].row
    xx=r[2].value

    #print(xx)
    yy=kkma.pos(xx)
    #print(yy)

    #sentences=xx.jki.morphAnalyzer(phrase)
    #morphemes=[]
    #if not sentences:
    #    morphemes
    
    b=""
    for j in range(0,int(len(yy))):
        b=b+yy[j][0]+""+yy[j][1]+" / "
    #print(b)
    ws.cell(row=row_index, column=5).value=b


wb.save('C:\\Program Files\\Python35\\크롤러\\insta.xlsx')
wb.close()
