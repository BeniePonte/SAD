from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField  # Ensure this is imported correctly

class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=False)
    location = forms.ChoiceField(
        choices=[
            ('girne', 'Girne'),
            ('lefkoşa', 'Lefkoşa'),
            ('lefke', 'Lefke'),
            ('iskele', 'İskele'),
            ('gazimağusa', 'Gazimağusa'),
            ('güzelyurt', 'Güzelyurt'),
        ],
        required=False,
    )
    captcha = CaptchaField()  # Add CAPTCHA field

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'location', 'password1', 'password2', 'captcha']

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()  # Add CAPTCHA field here
