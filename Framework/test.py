__author__ = 'sbedework'
# importing the required modules
# importing required modules
import PyPDF2

pdfFileObj = open('SP0032a_1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(1)

print(pageObj.extractText())