from PyPDF2 import PdfReader
 
def pdfExtract (loc):
    # creating a pdf reader object
    reader = PdfReader(loc)
    
    # printing number of pages in pdf file
    print(len(reader.pages))
    
    text=""
    # getting a specific page from the pdf file
    for i in range(len(reader.pages)):
        page = reader.pages[i]
    
        # extracting text from page
        text += page.extract_text()
        # print(text)
    return {"extract":text}