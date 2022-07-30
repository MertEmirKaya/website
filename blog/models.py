from unicodedata import name
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import  RichTextUploadingField
from django.urls import reverse


def upload_to(instance, filename):
    article_path=str(instance.title).replace(" ","")
    return f'articles/{article_path}/{filename}'

class Category(models.Model):
    name=models.CharField(max_length=99,null=True,blank=True)
    slug=models.SlugField(max_length=99,unique=True,null=True)

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self):
        return reverse("articlesByCategory", kwargs={"category_slug": self.slug})  # new                

class Article(models.Model):
    title= models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='category_slug')
    card_headline=models.CharField(max_length=100,null=True,blank=True)
    card_image=models.ImageField(null=True,blank=True,upload_to=upload_to)
    content_upload=RichTextUploadingField(blank=True,null=True)
    created_date=models.DateField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"category_slug": self.category.slug})  # new        