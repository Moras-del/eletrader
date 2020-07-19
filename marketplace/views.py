from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .filter import OrderFilter
from .forms import OrderCreationForm
from .models import Order
from PIL import Image
from marketplace.forms import FilterForm


class OrderList(ListView):
    model = Order
    template_name = 'marketplace/mainpage.html'
    context_object_name = 'orders'
    paginate_by = 12

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrderList, self).get_context_data(object_list=object_list, **kwargs)
        context["form"] = FilterForm(self.request.GET)
        return context

    def get_queryset(self):
        orders = super().get_queryset()
        form = FilterForm(self.request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            filter_items = {k: v for k, v in cd.items() if v is not None}
            my_filter = OrderFilter(filter_items)
            orders = my_filter.get_filtered_orders()
        return orders

class OrderDetail(DetailView):
    model = Order
    template_name = 'marketplace/orderdetail.html'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    query_pk_and_slug = True
    context_object_name = 'order'


class OrderCreation(View):

    def get(self, request):
        form = OrderCreationForm(initial={'quantity': 1})
        return render(request, 'marketplace/ordercreate.html', {"form": form})

    def post(self, request):
        form = OrderCreationForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.owner = request.user
            order.save()
            return redirect('marketplace:list')
        return render(request, 'marketplace/ordercreate.html', {"form": form})
