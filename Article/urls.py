from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('articles/',views.Articles_list, name='articles_list'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('category/<str:category_slug>/', views.list_of_articles_by_category, name='category_list'),

    path('tags/<str:tags_slug>/', views.tagged, name='tagged'),


    path('events/', views.events, name='events'),

    path('ranking/', views.instance_ranking, name='create'),
]
