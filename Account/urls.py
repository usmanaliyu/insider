from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('account/profile/',views.profile,name='profile'),
    path('profile/update', views.profileupdate, name='profileupdate'),
    path('signup_done', views.signup_done, name='signup_done'),
    path('user/<str:username>', views.UserList.as_view(), name='user-voice'),
    path('term-of-use',views.term_of_use, name='term_of_use'),
]
