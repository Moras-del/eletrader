from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', login_required(LogoutView.as_view()), name='logout'),
    path('', login_required(views.profile), name='profile'),
    path('<int:pk>', views.UserDetails.as_view(), name='user-details'),
    path('edit/', login_required(views.EditProfile.as_view()), name="edit"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]

