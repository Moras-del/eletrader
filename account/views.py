from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView
from .models import Profile
from .forms import UserForm, EditProfileForm
from .email_confirmation import send_email, TokenGenerator
from message.models import Message
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib import messages

class RegisterView(View):

    def get(self, request):
        user_form = UserForm()
        return render(request, 'account/register.html', {'form': user_form})

    def post(self, request):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.is_active = False
            new_user.save()
            send_email(request, new_user)
            return redirect('marketplace:list')
        return render(request, 'account/register.html', {'form': user_form})

class EditProfile(View):

    def get(self, request):
        form = EditProfileForm(instance=request.user)
        return render(request, "account/edit.html", {"form": form})

    def post(self, request):
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:profile')
        return render(request, "account/edit.html", {"form": form})

class UserDetails(DetailView):
    model = Profile
    template_name = 'account/user.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'user'

def profile(request):
    active_messages = Message.get_active_messages(request.user)
    return render(request, 'account/profile.html', {"active_messages": active_messages})

def activate(request, uidb64, token):
    token_generator = TokenGenerator()
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = Profile.objects.get(pk=uid)

    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('account:login')
    else:
        messages.error(request, 'Activation link is invalid!')
    
    return redirect('marketplace:list')