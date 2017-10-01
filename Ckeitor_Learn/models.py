from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Image_up_RichField(models.Model):

    Id = models.AutoField(primary_key=True)
    Body = RichTextUploadingField(verbose_name=u'带图片上传功能的富文本编辑器')


class None_Image_up_RichField(models.Model):

    Id = models.AutoField(primary_key=True)
    Body = RichTextField(verbose_name=u'普通富文本编辑器')