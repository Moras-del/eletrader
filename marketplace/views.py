from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from .order_management import OrderManagement
from .forms import OrderCreationForm, SortForm, OrderEditForm, FilterForm
from .models import Order


class OrderList(ListView):
    model = Order
    template_name = 'marketplace/mainpage.html'
    context_object_name = 'orders'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrderList, self).get_context_data(object_list=object_list, **kwargs)
        context["filter"] = FilterForm(self.request.GET)
        context["sort"] = SortForm(self.request.GET)
        return context

    def get_queryset(self):
        orders = super().get_queryset()
        om = OrderManagement(orders)
        self.filter(om)
        self.sorter(om)
        return om.get_orders()

    def filter(self, om):
        filter_form = FilterForm(self.request.GET)
        if filter_form.is_valid():
            filter_cd = filter_form.cleaned_data
            filter_items = {k: v for k, v in filter_cd.items() if v is not None}
            om.filter_orders(filter_items)

    def sorter(self, om):
        sort_form = SortForm(self.request.GET)
        if sort_form.is_valid():
            sort_cd = sort_form.cleaned_data
            if sort_cd['sorting']:
                om.sort_orders(sort_cd)

class OrderDetail(DetailView):
    model = Order
    template_name = 'marketplace/orderdetail.html'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    query_pk_and_slug = True
    context_object_name = 'order'

    def get_object(self):
        order = super().get_object()
        if self.request.user.is_authenticated and self.request.user != order.owner:
            order.clicks.add(self.request.user)
            order.save()
        return order

class OrderEdit(View):

    def get(self, request, pk, slug):
        order = get_object_or_404(Order, pk=pk, slug=slug, owner=request.user)
        form = OrderEditForm(instance=order)
        return render(request, "marketplace/edit.html", {"form": form})

    def post(self, request, pk, slug):
        order = get_object_or_404(Order, pk=pk, slug=slug, owner=request.user)
        form = OrderEditForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('marketplace:detail', pk, slug)
        return render(request, "marketplace/edit.html", {"form": form})


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
