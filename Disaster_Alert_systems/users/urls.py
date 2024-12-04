from django.urls import path
from . import views  # This imports all views, allowing you to reference them like `views.register`

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),  
    path('register/', views.register, name='register'),  # Change register_user to register
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
]
