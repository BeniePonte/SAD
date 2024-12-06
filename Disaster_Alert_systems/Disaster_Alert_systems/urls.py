from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Gestion des utilisateurs
    path('alerts/', include('alerts.urls')),  # URLs liées aux alertes
    path('users/', include('users.urls')),  # Inclut les URLs de l'application 'users'
    path('captcha/', include('captcha.urls')),
    path('', RedirectView.as_view(url=reverse_lazy('users:landing')), name='root'),  # Redirection par défaut vers la landing page
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
