from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/',views.profile,name='profile'),
    path('profile/update', views.profileupdate, name='profileupdate'),
    path('signup_done', views.signup_done, name='signup_done')
]
