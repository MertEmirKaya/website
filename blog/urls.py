from django.urls import path
from .views import blog ,blog_detail,searchBar,articles_by_Category
urlpatterns = [
    path("",blog,name="blog"),
    path("category/<slug:category_slug>/",articles_by_Category,name="articlesByCategory"),
    path("<slug:category_slug>/<int:pk>",blog_detail,name='article_detail'),
    path('search/',searchBar,name='search'),
    
]