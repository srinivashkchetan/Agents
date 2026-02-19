#This python code is used to read a document and extract the text from it using openai api.
#open AI is used to respond to the user's question based on the text extracted from the document.
#The document is a PDF file.
#The text is extracted using the PyPDF2 library.
#The text is then saved to a text file.
#The text file is then read and the text is printed to the console.


import PyPDF2

def read_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

print(read_pdf('document.pdf'))
