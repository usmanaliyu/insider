from django.urls import path
from . import views


urlpatterns = [
    path('',views.home.as_view(), name='home'),
    path('articles/',views.articles, name='articles_list'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('category/', views.categorylist, name='category_list'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
]
