from django.urls import path
from . import views


urlpatterns = [
    path('',views.home.as_view(), name='home'),
    path('articles/',views.articles, name='articles_list'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('category/<str:category_slug>/', views.list_of_articles_by_category, name='category_list'),

    path('tags/<str:tags_slug>/', views.tagged, name='tagged'),

    #path('tag/<str:tags_slug>/', views.tag_list_view.as_view(), name='tagged'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
]
