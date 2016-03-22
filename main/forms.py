from django import forms
from django.contrib.auth import get_user_model

from .models import Player


class PlayerSignupForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ['user_name', 'contact_info',]