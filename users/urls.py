# users/urls.py
from django.urls import path
from . import views
from alerts import views as alert_views 

app_name = 'users' 

urlpatterns = [
    path('', views.landing_page, name='landing'),  
    path('login/', views.login_view, name='login'),  
    path('register/', views.register, name='register'),  
    path('logout/', views.logout_view, name='logout'),  
    path('home/', views.home, name='home'),
    path('alerts/', alert_views.alert_list, name='alert_list'),  
    path('alerts/view/', alert_views.disaster_alert_view, name='disaster_alert_view'), 
    path('contact/', views.contact, name='contact'), 
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
