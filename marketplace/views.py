from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_filters.views import FilterView
from .filters import OrderFilter
from .models import Order

class OrderList(FilterView):
    model = Order
    template_name = 'marketplace/orderlist.html'
    context_object_name = 'orders'
    filterset_class = OrderFilter


class OrderDetail(DetailView):
    model = Order
    template_name = 'marketplace/orderdetail.html'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    query_pk_and_slug = True
    context_object_name = 'order'


