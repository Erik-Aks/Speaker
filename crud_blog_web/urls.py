from django.urls import path

from crub_blog.urls import urlpatterns
from crud_blog_web.views import  index, indexArticle, indexArticleJson
urlpatterns=[
    parth('test/', index),
    path('html/', indexArticle),
    path('article/', indexArticleJson)
]