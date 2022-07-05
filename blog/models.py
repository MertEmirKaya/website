from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import  RichTextUploadingField

def upload_to(instance, filename):
    article_path=str(instance.title).replace(" ","")
    return f'articles/{article_path}/{filename}'


class Article(models.Model):
    title= models.CharField(max_length=100)
    subject=models.CharField(max_length=100,blank=True,null=True)
    card_headline=models.CharField(max_length=100,null=True,blank=True)
    card_image=models.ImageField(null=True,blank=True,upload_to=upload_to)
    content_upload=RichTextUploadingField(blank=True,null=True)
    created_date=models.DateField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.title