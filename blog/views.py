from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import Article

# Create your views here.

def blog(request):
    articles=Article.objects.all()
    return render(request,'blog/blog.html',{'articles':articles})

def blog_detail(request,pk):
    article= get_object_or_404(Article, id=pk)

    return render(request,'blog/blog-detail.html',{'article':article})