from django.urls import path
from . import views


urlpatterns = [
    path('business-listings/',views.Listing_list, name='listing_list'),
    path('business-listings/search/',views.listing_search, name='listing_search'),
    path('<str:listing_slug>/',views.listing_detail, name='listing_detail'),
    path('listings',views.list_home, name="listing_home"),
    path('createform', views.listcreate.as_view(), name='list_create'),
    path('<str:slug>/update', views.listupdate.as_view(), name='list_update'),
    path('<str:slug>/delete', views.listdelete.as_view(), name='list_delete'),
    path('products/<str:tags_slug>/', views.listtag, name='list_tag'),
    path('business/categories/<str:category_slug>/', views.list_of_business_by_category, name='business_category_list'),

]
