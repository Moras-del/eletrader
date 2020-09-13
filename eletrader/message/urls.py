from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "message"

urlpatterns = [
    path('<int:pk>/<slug:slug>/', login_required(views.MessageView.as_view()), name="messages-customer"),
    path('<int:pk>/<slug:slug>/<str:username>/', login_required(views.MessageView.as_view()), name="messages-owner"),
    path('senders/<slug:slug>/', login_required(views.senders_view), name="senders"),
]