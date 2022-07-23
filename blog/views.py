from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import Article
from django.db.models import Q
# Create your views here.

def blog(request):
    articles=Article.objects.all()
    return render(request,'blog/blog.html',{'articles':articles})

def blog_detail(request,pk):
    article= get_object_or_404(Article, id=pk)

    return render(request,'blog/blog-detail.html',{'article':article})


def searchBar(request):
    
    if request.method=='POST':
        searched=request.POST['searched']
        articles=Article.objects.filter(Q(title__contains=searched)|Q(subject__contains=searched)|Q(card_headline__contains=searched))
        return render(request,'blog/blog.html',{'articles':articles,'searched':searched})

    else:    
        pass
        # return render(request,'blog/blog-detail.html',{'articles':articles})  