from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'marketplace'

urlpatterns = [
    path('', views.OrderList.as_view(), name='list'),
    path('order/<int:pk>/<slug:slug>', views.OrderDetail.as_view(), name='detail'),
    path('order/new', views.OrderCreation.as_view(), name='create'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)