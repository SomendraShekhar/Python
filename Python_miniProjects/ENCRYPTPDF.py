from PyPDF2 import PdfFileReader, PdfFileWriter

pdf = PdfFileReader("file.pdf")

pdfwriter = PdfFileWriter()

for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPage(page_num))

password = "pythonhub"
pdfwriter.encrypt(password)

with open("newfile.pdf", 'wb') as f:
    pdfwriter.write(f)

f.close()
