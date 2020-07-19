from django.urls import path

from . import views

app_name = "message"

urlpatterns = [
    path('<int:pk>/<slug:slug>/', views.MessageView.as_view(), name="messages"),
    path('<int:pk>/<slug:slug>/<str:username>/', views.MessageView.as_view(), name="answer"),
    path('senders/<slug:slug>/', views.senders_view, name="senders"),
]