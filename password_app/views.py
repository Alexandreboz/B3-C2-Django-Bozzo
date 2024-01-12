from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Password

def password_list(request):
    passwords = Password.objects.all()
    return render(request, 'password_app/password_list.html', {'passwords': passwords})

class PasswordCreateView(CreateView):
    model = Password
    fields = ['site', 'username', 'password']
    template_name = 'password_app/password_form.html'
    success_url = reverse_lazy('password-list')

class PasswordUpdateView(UpdateView):
    model = Password
    fields = ['site', 'username', 'password']
    template_name = 'password_app/password_from.html'
    success_url = reverse_lazy('password-list')

class PasswordDeleteView(DeleteView):
    model = Password
    template_name = 'password_app/password_confirm_delete.html'
    success_url = reverse_lazy('password-list')
