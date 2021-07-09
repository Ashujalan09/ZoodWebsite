from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from homepage import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home)
]


