"""
URL configuration for password_manager project.

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
from password_app import views
# from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('passwords/', views.password_list, name='password-list'),

    path('passwords/create/', views.PasswordCreateView.as_view(), name='password-create'),

    path('passwords/<int:pk>/update/', views.PasswordUpdateView.as_view(), name='password-update'),

    path('passwords/<int:pk>/delete/', views.PasswordDeleteView.as_view(), name='password-delete'),
]
