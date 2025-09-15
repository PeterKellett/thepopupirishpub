from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('kiwobar', views.kiwobar, name='kiwobar'),
    path('guinnessbar', views.guinnessbar, name='guinnessbar'),
    path('mobilebar', views.mobilebar, name='mobilebar'),
    path('tabletopbar', views.tabletopbar, name='tabletopbar'),
]

