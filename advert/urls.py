from django.urls import path
from . import views


urlpatterns = [
    path('ad-guidelines/', views.AdGuidline, name='ad_guidelines'),
]
