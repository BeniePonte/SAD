from django.urls import path
from . import views  # This imports all views, allowing you to reference them like `views.register`
from .views import register, login_view
app_name = 'users'

urlpatterns = [
    path('', views.landing_page, name='landing'), 
    path('login/', views.login_view, name='login'),  
    path('register/', views.register, name='register'),  # Change register_user to register
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
]
