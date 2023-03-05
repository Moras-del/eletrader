from django import forms
from django.contrib.auth.models import User
from account.models import Profile
from material.base import Layout, Row


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Powtórz hasło', required=False)

    layout = Layout('username', 'email', Row('password', 'confirm_password'))

    class Meta:
        model = Profile
        fields = ('username', 'email')

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Hasła nie są identyczne')
        return cd['confirm_password']

class EditProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].label = "Numer telefonu"
        self.fields['phone_number'].required = False

    class Meta:
        model = Profile
        fields = ('phone_number', 'email')