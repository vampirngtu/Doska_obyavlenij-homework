from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Advertisement, Reply, OneTimeCode
from tinymce.widgets import TinyMCE


User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label=('Email'),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class AdvertisementForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Advertisement
        fields = ['category', 'title', 'description', 'price']


class VerifyForm(forms.ModelForm):
    class Meta:
        model = OneTimeCode
        fields = ['user', 'code']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['reply_text']