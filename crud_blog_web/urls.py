from django.urls import path
from crud_blog_web.views import index, indexArticle, indexArticleJson

urlpatterns = [
    path('', index, name='index'),  # Obsługa strony głównej "/"
    path('html/', indexArticle, name='html'),  # Ścieżka do widoku HTML
    path('article/', indexArticleJson, name='article'),  # Ścieżka do widoku JSON
]
