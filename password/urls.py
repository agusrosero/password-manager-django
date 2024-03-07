from django.urls import path
from . import views


urlpatterns = [
    path('', views.password_list, name='password_list'),
    path('add_password/', views.password_add, name='password_add'),
    path('password_delete/<int:id>/',
         views.password_delete, name='password_delete'),
]
