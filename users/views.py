from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import DisasterAlert, Location
from alerts.models import Alert
from alerts.models import DisasterAlert
from .models import Alert  
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash

def home(request):
    alerts = Alert.objects.all()
    return render(request, 'home.html', {'alerts': alerts})

def contact(request):
    return render(request, 'contact.html')
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:home')  
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Update the email
        request.user.email = email

        # Update the password if a new password is provided
        if password:
            request.user.set_password(password)

        # Save the changes
        request.user.save()

        # Update the session if the password was changed
        if password:
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Password updated successfully.')

        # Success message after profile update
        messages.success(request, 'Profile updated successfully!')
        return redirect('users:profile')

    return render(request, 'home')

@login_required
def alert_list(request):
    alerts = Alert.objects.all()  # Assuming you have an Alert model
    return render(request, 'alerts.html', {'alerts': alerts})

# View for a specific disaster alert
def disaster_alert_view(request):
    disaster_alerts = DisasterAlert.objects.all()  
    context = {'disaster_alerts': disaster_alerts}
    return render(request, 'alerts/disaster_alert_view.html', context)

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('users:login')
    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
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
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})
@login_required
def home(request):
    alerts = Alert.objects.all()  # Fetch all alerts from the database
    return render(request, 'home.html', {'alerts': alerts})

def logout_view(request):
    logout(request)
    return redirect('users:login')

def landing_page(request):
    return render(request, 'landing.html')

def user_logout(request):
    logout(request)
    return redirect('users:login')

# session 
def profile_view(request):
    user_id = request.session.get('user_id')  # Retrieve the user ID from the session
    if user_id:
        user = User.objects.get(id=user_id)  # Query the database for the user
        return render(request, 'home.html', {'user': user})
    else:
        return redirect('login')  # Redirect if no session exists
    

def password_reset(request):
    return render(request, 'password_reset.html')