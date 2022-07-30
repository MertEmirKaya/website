from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import Article,Category
from django.db.models import Q
# Create your views here.

def blog(request):
    articles=Article.objects.all()
    categories=Category.objects.all()

    return render(request,'blog/blog.html',{'articles':articles,'categories':categories})

def articles_by_Category(request,category_slug):
    articles=Article.objects.filter(category__slug=category_slug)
    categories=Category.objects.all()
    return render(request,'blog/blog.html',{'articles':articles,'categories':categories})

def blog_detail(request,pk,category_slug):
    article= get_object_or_404(Article, id=pk,category__slug=category_slug)

    return render(request,'blog/blog-detail.html',{'article':article})


def searchBar(request):
    
    if request.method=='POST':
        searched=request.POST['searched']
        articles=Article.objects.filter(Q(title__contains=searched)|Q(category__slug__contains=searched)|Q(card_headline__contains=searched))
        return render(request,'blog/blog.html',{'articles':articles,'searched':searched})

    else:    
        pass
        # return render(request,'blog/blog-detail.html',{'articles':articles})  