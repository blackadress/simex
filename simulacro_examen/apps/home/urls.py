from django.urls import path, re_path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.ViewLogin.as_view(), name='view_login'),
]
