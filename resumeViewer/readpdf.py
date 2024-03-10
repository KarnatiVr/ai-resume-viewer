from pypdf import PdfReader 
  
# creating a pdf reader object 
reader = PdfReader('Venkatraja_Fresher.pdf') 
  
# printing number of pages in pdf file 
print(len(reader.pages)) 
  
# getting a specific page from the pdf file 
page = reader.pages[1] 
  
# extracting text from page 
text = page.extract_text() 
print(text) 