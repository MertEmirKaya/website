from django.urls import path
from .views import blog ,blog_detail,searchBar
urlpatterns = [
    path("",blog,name="blog"),
    path("<int:pk>",blog_detail,name='blog_detail'),
    path('search',searchBar,name='search')
]