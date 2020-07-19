from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.profile, name='profile'),
    path('edit/', views.EditProfile.as_view(), name="edit"),
]

