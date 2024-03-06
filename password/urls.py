from django.urls import path
from . import views


urlpatterns = [
    path('', views.password_list, name='password_list'),
    path('add_password/', views.password_add, name='password_add'),
]
