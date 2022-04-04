import PyPDF2
pdf_obj=open('test.pdf','rb')
pdfread = PyPDF2.PdfFileReader(pdf_obj)
x=pdfread.numPages
page_obj=pdfread.getPage(x-1)
text=page_obj.extractText()
#print(text)

file =open(r"D:\\AB projects\\Automation\\linkedin_login\\1.txt","a")
file.writelines(text)
file.close()