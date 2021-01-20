# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image
import sys,os
import imp

imp.reload(sys)
inputFileName=sys.argv[1]
outputFileName=sys.argv[2]

app_dir=os.path.realpath(os.path.dirname(sys.argv[0]))

output_file = PdfFileWriter()
file_=open(inputFileName, "rb")
input_file = PdfFileReader(file_)


page_count = input_file.getNumPages()
lastPage=input_file.getPage(page_count-1)
pageMediaBox=input_file.getPage(page_count-1).mediaBox


from reportlab.pdfgen import canvas	
c = canvas.Canvas(app_dir+r'watermark.pdf')
c.setPageSize((float(pageMediaBox.getWidth()),float(pageMediaBox.getHeight())))
if pageMediaBox.getWidth()>pageMediaBox.getHeight():
    c.drawImage(app_dir+r'\MAIN.png', float(pageMediaBox.getWidth())-420, float(pageMediaBox.getHeight())-565,65*3,35*3,mask='auto')
    c.drawImage(app_dir+r'\BUH.png', float(pageMediaBox.getWidth())-220, float(pageMediaBox.getHeight())-565,65*3,35*3,mask='auto')
else:
    c.drawImage(app_dir+r'\MAIN.png', float(pageMediaBox.getWidth())-420, float(pageMediaBox.getHeight())-825,65*3,35*3,mask='auto')
    c.drawImage(app_dir+r'\BUH.png', float(pageMediaBox.getWidth())-220, float(pageMediaBox.getHeight())-825,65*3,35*3,mask='auto')
c.save()
watermark = PdfFileReader(open(app_dir+r"watermark.pdf", "rb"))


for page_number in range(page_count):
    input_page = input_file.getPage(page_number)
    if page_number==page_count-1:
        input_page.mergePage(watermark.getPage(0))
    output_file.addPage(input_page)
with open(outputFileName, "wb") as outputStream:
    output_file.write(outputStream)
file_.close()
