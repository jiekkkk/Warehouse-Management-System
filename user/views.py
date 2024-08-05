from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm , UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created. You can now log in.')
            return redirect('user-login')
    else:
        form = CreateUserForm() 
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

def profile(request):
    context = {

    }
    return render(request, 'user/profile.html', context)


def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'user/profile_update.html', context)

def logout(request):
    context = {

    }
    return render(request, 'user/logout.html', context)