from django.contrib import admin
from django.urls import path
from .views import home,upload_resume,feedback_ready

urlpatterns = [
    path('', home, name='homepage'),
    path('upload',upload_resume,name='upload'),
    path('getfeedback',feedback_ready,name='feedback_ready')
]
