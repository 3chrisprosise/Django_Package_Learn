# django-Ckeditor

from django.shortcuts import render
from django.forms import modelformset_factory
from ckeditor_uploader.fields import RichTextUploadingField
from  ckeditor.fields import RichTextFormField

# Create your views here.

def editor(req):
    return render(req, 'Ckeditor.html')
