from django.urls import path
from .views import blog ,blog_detail,searchBar
urlpatterns = [
    path("",blog,name="blog"),
    path("<slug:category_slug>/<int:pk>",blog_detail,name='article_detail'),
    path('search',searchBar,name='search'),
    
]