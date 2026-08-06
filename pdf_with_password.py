from pypdf import PdfReader, PdfWriter
reader = PdfReader("") #enter the pdf file name which you want to protect 
writer = PdfWriter()

writer.append(reader)
writer.encrypt("") # enter a password you want

with open("protected.pdf", "wb") as file : writer.write(file)