from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from celery import shared_task
from pypdf import PdfReader 
import pathlib
import textwrap
from .models import User
import google.generativeai as genai


genai.configure(api_key="AIzaSyCS5HSz39mib7aGO4lr2EvzFtcMkD8ADGg")

model = genai.GenerativeModel('gemini-pro')


@shared_task
def get_feedback(text,id):
    response = model.generate_content("send me feedback on this resume"+text)
    print("response =>",response)
  # to_markdown(response.text)
    user=User.objects.get(pk=id)

    res=''
    with open('output.txt', 'w') as f:
        for chunk in response:
            f.write(chunk.text)
            f.write("\n" + "_"*80 + "\n")
            res+=chunk.text

    user.feedback=res
    user.save()
    


# creating a pdf reader object 
@shared_task
def extract_text_from_pdf(id):
    resume = User.objects.get(pk=id).resume
    reader = PdfReader(resume) 
    
    # printing number of pages in pdf file 
    print(len(reader.pages)) 
    
    # getting a specific page from the pdf file 
    page = reader.pages[1] 
    
    # extracting text from page 
    text = page.extract_text()
    print("text extracted from pdf")
    print("-------------------------------------") 
    print(text) 
    get_feedback(text,id)


