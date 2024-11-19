from . import views
from django.urls import path

app_name = 'article'
urlpatterns = [
    path('article_list/',views.article_list,name='article_list'),
    path('create_article/',views.create_article,name='create_article'),
    path('article/<slug:slug>/',views.article_detail,name='article_detail'),
] 