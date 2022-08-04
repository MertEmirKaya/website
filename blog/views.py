from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import Article,Category,Tag
from django.db.models import Q

from django.core.paginator import Paginator

def blog(request):
    articles=Article.objects.all()
    categories=Category.objects.all()
    p=Paginator(articles,4)
    page=request.GET.get('page')    
    articlesp=p.get_page(page)

    return render(request,'blog/blog.html',{'articles':articles,'articlesp':articlesp,'categories':categories})

def articles_by_Category(request,category_slug):
    articles=Article.objects.filter(category__slug=category_slug)
    categories=Category.objects.all()
    p=Paginator(articles,4)
    page=request.GET.get('page')    
    articlesp=p.get_page(page)
    return render(request,'blog/blog.html',{'articles':articles,'categories':categories,'articlesp':articlesp})

def blog_detail(request,pk,category_slug):
    article= get_object_or_404(Article, id=pk,category__slug=category_slug)
    articles=Article.objects.all()[0:4]
    categories=Category.objects.all()
    tags=Tag.objects.all()
    
    return render(request,'blog/blog-detail.html',{'articles':articles,'article':article,'categories':categories,'tags':tags})


def searchBar(request):
    articles=Article.objects.all()
    categories=Category.objects.all()
    p=Paginator(articles,4)
    page=request.GET.get('page')    
    articlesp=p.get_page(page)
    if request.method=='POST':
        searched=request.POST['searched']
        articlesp=Article.objects.filter(Q(title__contains=searched)|Q(category__slug__contains=searched)|Q(card_headline__contains=searched)|Q(tags__name__contains=searched)).distinct()
        return render(request,'blog/blog.html',{'articlesp':articlesp,'categories':categories})

    else:    
        pass
        # return render(request,'blog/blog-detail.html',{'articles':articles})  