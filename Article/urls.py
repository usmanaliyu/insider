from django.urls import path
from django.views.decorators.cache import cache_page
from . import views


urlpatterns = [
    path('',cache_page(60 * 15)(views.home),name='home'),
    path('articles/',views.Articles_list, name='articles_list'),
    path('article/<str:article_slug>', views.detail, name='detail'),
    path('categories/<str:category_slug>/', views.list_of_articles_by_category, name='category_list'),

    path('tags/<str:tags_slug>/', views.tagged, name='tagged'),
    path('search',views.search, name='search'),


    path('events/', views.events, name='events'),

]
