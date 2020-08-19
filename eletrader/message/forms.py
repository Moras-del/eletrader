from django import forms

from .models import Message

class CreateMessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('content',)