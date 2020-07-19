from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import UserForm, EditProfileForm


class RegisterView(View):

    def get(self, request):
        user_form = UserForm()
        return render(request, 'account/register.html', {'form': user_form})

    def post(self, request):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('account:profile')

def profile(request):
    return render(request, 'account/profile.html')


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