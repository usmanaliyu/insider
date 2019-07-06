from django.urls import path
from . import views


urlpatterns = [
    path('',views.Listing_list, name='listing_home'),
]
