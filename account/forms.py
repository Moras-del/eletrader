from django import forms
from django.contrib.auth.models import User
from account.models import Profile
from material import Layout, Row


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Powtórz hasło')

    layout = Layout('username', 'email', Row('password', 'confirm_password'))

    class Meta:
        model = Profile
        fields = ('username', 'email')

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Hasła nie są identyczne')
        return cd['confirm_password']