from django.urls import path
from . import views


urlpatterns = [
    path('business-listings/',views.Listing_list, name='listing_home'),
    path('<str:listing_slug>/',views.listing_detail, name='listing_detail'),
]
