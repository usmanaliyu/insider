from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('articles/',views.articles, name='articles_list'),
    path('detail/', views.detail, name='detail'),
    path('category/', views.categorylist, name='categorylist'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
]
