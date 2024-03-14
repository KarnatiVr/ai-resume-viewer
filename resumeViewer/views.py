from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .tasks import extract_text_from_pdf
from .forms import ResumeForm
from .models import User
# Create your views here.
id=''
def home(request):
    return render(request,'home.html')

def upload_resume(request):
    if request.method == 'POST':

        form = ResumeForm(request.POST,request.FILES)
        # check whether it's valid:
        # print(form.is_valid())
        # resume=request.FILES['resume']

        if form.is_valid():
            # User.objects.create()
            resume=request.FILES['resume']
            name=request.POST['name']
            if resume is not None:  
                user_instance = User.objects.create(name=name,resume=resume)
                user_instance.save()
                extract_text_from_pdf.delay(user_instance.id) 
                return render(request, 'upload.html',{'form_submitted':True,'show':False})      

        else:
            print(form.errors)  # Print form errors to console for debugging
            return HttpResponse("Error", content_type='text/plain')
    else:
        form = ResumeForm()
        return render(request, 'upload.html',{'form':form,'form_submitted':False,'show':False})
    
def feedback_ready(request):
        form = ResumeForm()
        with open('output.txt', 'r') as file:

            feedback= file.read()
        
        with open('output.txt', 'w') as file:

            file.write('')


        return render(request, 'upload.html',{"feedback":feedback,'show':False})
