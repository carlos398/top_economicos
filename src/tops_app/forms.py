from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    """FORM FOR USER REGISTER"""
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = UserProfile
        fields = ['email', 'name', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
