from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests  # Ensure this is installed and imported for the reCAPTCHA verification

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('users:login')
        else:
            for field, errors in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {', '.join(errors)}")
    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form': form})


def verify_recaptcha(recaptcha_response):
    """
    Verify reCAPTCHA response using Google's API.
    """
    secret_key = '6LdgoZIqAAAAACm5KXxlZHjwdsZrDBnnNGg2IllL'  # Replace with your actual secret key
    payload = {
        'secret': secret_key,
        'response': recaptcha_response
    }
    try:
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
        result = response.json()
        return result.get('success', False)
    except requests.exceptions.RequestException:
        return False


def login_view(request):
    """
    Handle user login with reCAPTCHA verification.
    """
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        if not recaptcha_response or not verify_recaptcha(recaptcha_response):
            messages.error(request, "Please complete the reCAPTCHA or ensure it's verified.")
            return redirect('users:login')

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('users:login')
