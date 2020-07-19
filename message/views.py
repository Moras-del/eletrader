from django.contrib.auth.models import User
from django.forms import ModelForm
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
        form = CreateMessageForm()
        return render(request, "message/messages.html", {"form": form, "messages": messages, "order": order})

    def post(self, request, pk, slug, username=None):
        order = get_object_or_404(Order, pk=pk, slug=slug)
        user = None
        if username is not None:
            user = get_object_or_404(Profile, username=username)
        form = CreateMessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.user_from = request.user
            if user is None:
                new_message.user_to = order.owner
            else:
                new_message.user_to = user
            new_message.order = order
            new_message.save()
        messages = self.get_all_messages(request, order, username)
        return render(request, "message/messages.html", {"form": form, "messages": messages, "order":order})

    def get_all_messages(self, request, order, username):
        if username is None:
            users = [request.user, order.owner]
        else:
            user = get_object_or_404(Profile, username=username)
            users = [request.user, user]
        return Message.objects.filter(order=order, user_from__in=users, user_to__in=users)


def senders_view(request, slug):
    order = get_object_or_404(Order, slug=slug)
    senders = set([message.user_from for message in order.messages.all() if message.user_to == order.owner])
    return render(request, "message/senderslist.html", {"senders": senders, "order": order})


