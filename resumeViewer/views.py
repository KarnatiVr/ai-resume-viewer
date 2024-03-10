from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ResumeForm
from .models import User
# Create your views here.

def home(request):
    return render(request,'home.html')

def upload_resume(request):
    if request.method == 'POST':

        form = ResumeForm(request.POST,request.FILES)
        # check whether it's valid:
        # print(form.is_valid())
        if form.is_valid():
            # User.objects.create()
            return HttpResponse("thanks for submitting the form", content_type='text/plain')
        else:
            print(form.errors)  # Print form errors to console for debugging
            return HttpResponse("Error", content_type='text/plain')
    else:
        form = ResumeForm()
        return render(request, 'upload.html',{'form':form})