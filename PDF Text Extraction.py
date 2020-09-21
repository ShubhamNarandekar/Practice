from PyPDF2 import PdfFileReader

file=open('C:/Users/ssnar/Downloads/msc.pdf','rb')
reader=PdfFileReader(file)
print('PDF Information =',reader.getDocumentInfo())
robj=reader.getNumPages()
for i in range(0, robj):
    print('\n-------------',i+1)
    obj=reader.getPage(i)
    s=obj.extractText()
    print(s)
    


file.close()