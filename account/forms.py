from django import forms
from django.contrib.auth.models import User
from account.models import Profile
from material.base import Layout, Row


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm password', required=False)

    layout = Layout('username', 'description', 'phone_number', 'email', Row('password', 'confirm_password'))

    class Meta:
        model = Profile
        fields = ('username', 'email', 'description', 'phone_number')

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Passwords do not match!')
        return cd['confirm_password']

class EditProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].label = "Phone number"

    class Meta:
        model = Profile
        fields = ('description', 'phone_number', 'email')