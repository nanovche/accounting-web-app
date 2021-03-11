from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import *
from django.contrib.auth.views import LoginView


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Акаунтът ви беше успешно създаден! Влезте сега !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    return render(request, template_name='users/profile.html')


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm



