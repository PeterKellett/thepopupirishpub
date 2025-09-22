from django.contrib import admin
from django.urls import path
from . import views
# from .views import SuccessView, ContactView

urlpatterns = [
    path('', views.index, name='home'),
    path('kiwobar', views.kiwobar, name='kiwobar'),
    path('guinnessbar', views.guinnessbar, name='guinnessbar'),
    path('mobilebar', views.mobilebar, name='mobilebar'),
    path('tabletopbar', views.tabletopbar, name='tabletopbar'),
    # path("contact/", ContactView.as_view(), name="contact"),
    # path("success/", SuccessView.as_view(), name="success"),

]

