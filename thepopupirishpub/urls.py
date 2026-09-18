"""
URL configuration for thepopupirishpub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns # <-- Import i18n_patterns

# 1. Base URL patterns that shouldn't change with language
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')), # <-- Required for the language switcher form to work
]

# 2. Localized URL patterns that get prefixed (e.g., /de/, /fr/)
urlpatterns += i18n_patterns(
    path('', include('home.urls')),
    prefix_default_language=True # Forces /en/ for the English site. Set to False if you want English to stay clean (e.g. ://site.com)
)

# 3. Media files asset serving (only used in development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
