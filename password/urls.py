from django.urls import path
from . import views


urlpatterns = [
    path('', views.password_list, name='password_list'),
]
