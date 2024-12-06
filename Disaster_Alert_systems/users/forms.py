from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from captcha.fields import CaptchaField
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()  # Add CAPTCHA to the login form

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

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'location', 'password1', 'password2']
