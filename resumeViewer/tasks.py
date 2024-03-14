from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from celery import shared_task
from pypdf import PdfReader 
import pathlib
import textwrap
from .models import User
import google.generativeai as genai
# from docx import Document
# import subprocess
# import os


genai.configure(api_key="AIzaSyAnAhl2HDXxCJXIOdJMeI5oJ-QOLv8C51o")

model = genai.GenerativeModel('gemini-pro')




@shared_task
def get_feedback(text,id):
    response = model.generate_content("send me feedback of this resume"+text)
    print("response =>",response)
    # user=User.objects.get(pk=id)

    # res=''
    with open('output.txt', 'w') as f:
        for chunk in response:
            f.write(chunk.text)
            f.write("\n" + "_"*80 + "\n")
            # res+=chunk.text

    # user.feedback=response
    # user.save()
    


# def convert_to_pdf(input_file, output_file):
#     # Check if the input file exists
#     if not os.path.exists(input_file):
#         print(f"Error: Input file '{input_file}' not found.")
#         return

#     # Define the LibreOffice command
#     libreoffice_cmd = [
#         "libreoffice",
#         "--headless",         # Run LibreOffice in headless mode
#         "--convert-to", "pdf",  # Convert to PDF format
#         "--outdir", os.path.dirname(output_file),  # Output directory
#         input_file            # Input file path
#     ]

#     # Execute the LibreOffice command
#     try:
#         subprocess.run(libreoffice_cmd, check=True)
#         print(f"Conversion successful: {input_file} -> {output_file}")
#     except subprocess.CalledProcessError as e:
#         print(f"Error: Conversion failed - {e}")



# creating a pdf reader object 
@shared_task
def extract_text_from_pdf(id):
    resume = User.objects.get(pk=id).resume
    print("resume name =>",resume)
    if(resume.name.split('.')[1] == 'pdf'):
        print("this is a pdf file")
    elif(resume.name.split('.')[1] == 'docx'):
        print("this is a docx file")
        return
    
    reader = PdfReader(resume)

# printing number of pages in pdf file 
    print(len(reader.pages)) 
    
    # getting a specific page from the pdf file 
    # page = reader.pages[1] 
    text=''
    # extracting text from pages
    for page in reader.pages:
        # print("text -----------------------",text) 
        text += page.extract_text()

    print("text extracted from pdf")
    print("-------------------------------------") 
    print(text) 
    get_feedback(text,id)


