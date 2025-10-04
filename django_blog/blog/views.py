# blog/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegistrationForm, UserUpdateForm, ProfileForm

def register_view(request):
    if request.user.is_authenticated:
        return redirect('blog:profile')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user after registration
            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect('blog:profile')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'  # optional; Django will redirect by default

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('blog:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileForm(instance=user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'blog/profile.html', context)
