from django.urls import path
from .views import blog ,blog_detail
urlpatterns = [
    path("",blog,name="blog"),
    path("<int:pk>",blog_detail,name='blog_detail')
]