# django-Ckeditor

from django.shortcuts import render

# Create your views here.

def editor(req):
    return render(req, 'Ckeditor.html')