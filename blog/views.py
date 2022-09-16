from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import Article,Category,Tag
from django.db.models import Q
from random import shuffle
from django.core.paginator import Paginator

def blog(request):
    articles=Article.objects.all()
    categories=Category.objects.all()
    p=Paginator(articles,4)
    page=request.GET.get('page')    
    articlesp=p.get_page(page)
    tags=Tag.objects.all()
    return render(request,'blog/blog.html',{'articles':articlesp,'categories':categories,'tags':tags})

def articles_by_Category(request,category_slug):
    articles=Article.objects.filter(category__slug=category_slug)
    categories=Category.objects.all()
    p=Paginator(articles,4)
    page=request.GET.get('page')    
    articlesp=p.get_page(page)
    return render(request,'blog/blog.html',{'categories':categories,'articles':articlesp})

def articles_by_tags(request,tag):
    articles=Article.objects.filter(tags__name__contains=tag)
    categories=Category.objects.all()
    p=Paginator(articles,4)
    page=request.GET.get('page')        
    articlesp=p.get_page(page)
    return render(request,'blog/blog.html',{'categories':categories,'articles':articlesp})

def blog_detail(request,article_slug,category_slug):
    article= get_object_or_404(Article,slug=article_slug,category__slug=category_slug)
    pk=article.id
    articles=Article.objects.exclude(id__in=[pk]).order_by('?')[0:5]
    categories=Category.objects.all()
    tags=Tag.objects.all()
    article_tags=Tag.objects.filter(tags=pk)
    return render(request,'blog/blog-detail.html',{'article':article,'categories':categories,'tags':tags,'articles':articles,'article_tags':article_tags})


def searchBar(request):     
    articles=Article.objects.all()
    categories=Category.objects.all()
    p=Paginator(articles,4)
    page=request.GET.get('page')    
    articlesp=p.get_page(page)
    if request.method=='POST':
        searched=request.POST['searched']
        articlesp=Article.objects.filter(Q(title__contains=searched)|Q(category__slug__contains=searched)|Q(card_headline__contains=searched)|Q(tags__name__contains=searched)).distinct()
        print(articlesp)
        return render(request,'blog/blog.html',{'articles':articlesp,'categories':categories})

    else:    
        pass
        # return render(request,'blog/blog-detail.html',{'articles':articles})  