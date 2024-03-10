from django import forms


class ResumeForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=200)
    resume= forms.FileField(label="Upload Resume")