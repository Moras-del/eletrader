from django.contrib.auth.models import User
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from message.forms import CreateMessageForm
from marketplace.models import Order
from message.models import Message
from account.models import Profile


class MessageView(View):

    def get(self, request, pk, slug, username=None):
        order = get_object_or_404(Order, pk=pk, slug=slug)
        messages = self.get_all_messages(request, order, username)
        messages.update(is_active=False)
        form = CreateMessageForm()
        return render(request, "message/messages.html", {"form": form, "messages": messages, "order": order})

    def post(self, request, pk, slug, username=None):
        order = get_object_or_404(Order, pk=pk, slug=slug)
        form = CreateMessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.user_from = request.user
            new_message.user_to = order.owner if username is None else get_object_or_404(Profile, username=username)
            new_message.order = order
            new_message.save()
            form = CreateMessageForm()
        messages = self.get_all_messages(request, order, username)
        return render(request, "message/messages.html", {"form": form, "messages": messages, "order":order})

    def get_all_messages(self, request, order, username):
        users = [request.user, order.owner if username is None else get_object_or_404(Profile, username=username)]
        return Message.objects.filter(order=order, user_from__in=users, user_to__in=users)


def senders_view(request, slug):
    order = get_object_or_404(Order, slug=slug, owner=request.user)
    senders = {}
    for message in order.messages.filter(user_to=request.user):
        senders[message.user_from] = order.get_active_messages(message.user_from)
    return render(request, "message/senders.html", {"senders": senders, "order": order})
