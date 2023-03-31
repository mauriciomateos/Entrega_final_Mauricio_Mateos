from django.contrib.auth.forms import UserCreationForm
from django import forms
from myapp.models import Page,Message
class RegisterForm(UserCreationForm):
    pass

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ('author', )

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('user_from', )